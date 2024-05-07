import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from http import client
from fastapi import FastAPI
from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process
import os
import requests


app = FastAPI()
#Liste des domaines autorisés, '*' signifie tout domaine
origins = [
    "http://localhost:4200",
    "http://localhost:81",
    "*",
]

# Configuration du middleware CORS                              
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Les origines autorisées
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PUT"],  # Les méthodes autorisées
    allow_headers=["X-Requested-With", "Content-Type"],  # Les en-têtes autorisés
)

@app.get("/getbestbeers/{meal}")
def requestApi(meal:str):
    output =  requestBestBeers(meal)
    print(output)
    return output





os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] ='llama3-8b-8192'  # Adjust based on available model
os.environ["OPENAI_API_KEY"] ='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'

def extract_json(api_response):
    # Trouver le début et la fin du JSON en supprimant les guillemets externes et le texte supplémentaire
    start = api_response.find('[')
    end = api_response.rfind(']') + 1
    # Extraire la sous-chaîne qui est le JSON valide
    json_string = api_response[start:end]
    # Convertir la chaîne JSON en objet Python
    data = json.loads(json_string)
    return data

def extract_brewery_description(beer_list):
    """
    Cette fonction prend en entrée une liste de dictionnaires, chaque dictionnaire contenant diverses informations sur une bière.
    Elle retourne une seule chaîne de caractères où chaque "Brewery" est associée à sa "Description".
    """
    result = []
    for beer in beer_list:
        # On construit la chaîne "Brewery - Description" pour chaque bière et on l'ajoute à la liste
        result.append('[')
        if "Brewery" in beer and "Description" in beer:
            result.append(f"{beer['Brewery']},")
    # On joint toutes les chaînes de la liste en les séparant par une nouvelle ligne
    result.append(']')
    return ''.join(result)


def requestBestBeers(meal:str):
    url = "http://api_beers:2711/beers"
    # Envoi de la requête GET
    response = requests.get(url)

    # Assurez-vous que la réponse est valide et récupérez le contenu JSON
    if response.status_code == 200:
        data = response.json()  # Cette méthode convertit directement le JSON en dictionnaire Python
        beers = extract_brewery_description(data)

    classifier = Agent(
        role = f"Sending JSON of the best three beers for a '{meal}'",
        goal = f"Choosing from this list [{beers}] the best three beers for a '{meal}'",
        backstory ="You are an REST API who provide JSON, you like to help people by choosing appropriate beat for their meal",
        verbose = True,
        allow_delegation = False,
    )

    classify_beers = Task(
        description = f"Get the perfect three beers for this meal '{meal}'",
        agent = classifier,
        expected_output = "A JSON structured like that: [{'BeerName':'string', 'Description':'string'}]. Description has to be in french"
    )

    crew = Crew(
        agents= [classifier],
        tasks= [classify_beers],
        verbose=1,
        process= Process.sequential
    )

    output = crew.kickoff()
    result = extract_json(classify_beers.output.raw_output)
    stringJson = json.dumps(result)
    return result


