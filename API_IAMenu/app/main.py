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

@app.get("/getMenu")
def requestApi():
    output =  requestBestBeers()
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

def extract_meal_description(meal_list: dict):
    """
    Cette fonction prend en entrée une liste de dictionnaires, chaque dictionnaire contenant diverses informations sur une bière.
    Elle retourne une seule chaîne de caractères où chaque "Brewery" est associée à sa "Description".
    """
    result = []
    result.append('[')
    for beer in meal_list.values():
        # On construit la chaîne "Brewery - Description" pour chaque bière et on l'ajoute à la liste
        result.append(f"{beer['id']}-{beer['nom_de_plat']};")
    # On joint toutes les chaînes de la liste en les séparant par une nouvelle ligne
    result.append(']')
    return ''.join(result)

def extract_brewery_description(beer_list):
    """
    Cette fonction prend en entrée une liste de dictionnaires, chaque dictionnaire contenant diverses informations sur une bière.
    Elle retourne une seule chaîne de caractères où chaque "Brewery" est associée à sa "Description".
    """
    result = []
    result.append('[')
    for beer in beer_list:
        # On construit la chaîne "Brewery - Description" pour chaque bière et on l'ajoute à la liste
        result.append(f"{beer['Id']} - {beer['Name']};")
    # On joint toutes les chaînes de la liste en les séparant par une nouvelle ligne
    result.append(']')
    return ''.join(result)

def getMealsFromAPI():
    url = "http://api_plats:80/api/plats"
    # Envoi de la requête GET
    response = requests.get(url)

    # Assurez-vous que la réponse est valide et récupérez le contenu JSON
    if response.status_code == 200:
        data = response.json()  # Cette méthode convertit directement le JSON en dictionnaire Python
        beers = extract_meal_description(data)
        return beers

def getBeersFromAPI():
    url = "http://api_beers:2711/beers"
    # Envoi de la requête GET
    response = requests.get(url)

    # Assurez-vous que la réponse est valide et récupérez le contenu JSON
    if response.status_code == 200:
        data = response.json()  # Cette méthode convertit directement le JSON en dictionnaire Python
        beers = extract_brewery_description(data)
        return beers

def requestBestBeers():
    
    beers = getBeersFromAPI()
    meals = getMealsFromAPI()
    classifier = Agent(
        role = f"Sending JSON of one best combination between a beer and a meal'",
        goal = f"Choosing the perfect combination between a meal form this list '{meals}' and a beer from this list '{beers}''",
        backstory ="You are an REST API who provide JSON, you like to help people by choosing the perfect menu",
        verbose = True,
        allow_delegation = False,
    )

    classify_beers = Task(
        description = f"Get the perfect combination between a meal form this list '{meals}' and a beer from this list '{beers}, you have to generate only one menu'",
        agent = classifier,
        expected_output = "A JSON structured like that: [{'IdBeer':'Integer', BeerName':'string', 'IdMeal':'Integer', MealName':'string', 'Explanation':'string'}]. Explanation has to be in french"
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


