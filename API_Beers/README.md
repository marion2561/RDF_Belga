# API des Bières Belges

L'API des Bières Belges offre un service web simple pour récupérer une liste de bières belges filtrées par un pourcentage minimum d'alcool par volume (ABV). Elle est construite en utilisant Flask, un framework web léger pour Python, et utilise Pandas pour la gestion des données.

## Fonctionnalités

- **Obtenir des bières par ABV minimum et type** : Permet aux clients de récupérer la liste des bières disponibles et de choisir un taux d'alcool supérieur ou égal à un minimum spécifié et/ou qu'un certain type de bière.

- **Obtenir une recommandation de 10 bières** : Permet aux clients de demander une suggestion de 10 bières du moment.

## Prérequis

Pour exécuter l'API, vous aurez besoin des éléments suivants :
- Python 3.6 ou supérieur
- Flask
- Pandas
- Flask-CORS

Vous pouvez installer les bibliothèques nécessaires avec pip :

```bash
pip install -r requirements.txt
```
## Configuration et Installation

1. **Cloner le Répertoire :**

```bash
git clone https://github.com/marion2561/RDF_Belga/beer_services.git

cd beer_services
```

2. **Préparer les Données :**

Assurez-vous d'avoir un fichier CSV nommé ```beers.csv``` dans le répertoire racine du projet. Le fichier CSV doit comporter au moins les colonnes suivantes :
- ```Name``` : Le nom de la bière.
- ```ABV``` : Le pourcentage d'alcool par volume.
- ```Type``` : Le type de bière.
- ```Brewery``` : La brasserie qui produit la bière.
- ```Description``` : Une brève description de la bière.
- ```Image_URL``` : Un URL d'image pour la bière

3. **Exécution de l'API :**

Lancez l'application Flask en exécutant :

```bash
python beer_service.py
```

## Utilisation

Pour récupérer toutes les bières, envoyez une requête GET à l'endpoint ```/beers```
```bash
curl http://127.0.0.1:2711/beers
```
> *Cette requête retournera toutes les bières*

Pour récupérer des bières par ABV minimum, envoyez une requête GET à l'endpoint ```/beers``` avec le paramètre de requête ```min_abv``` :
```bash
curl http://127.0.0.1:2711/beers?min_abv=8
```
> *Cette requête retournera toutes les bières avec un ABV de 8% ou plus.*

Pour récupérer des bières par Type, envoyez une requête GET à l'endpoint ```/beers``` avec le paramètre de requête ```type``` :
```bash
curl http://127.0.0.1:2711/beers?type=Blonde
```
> *Cette requête retournera toutes les bières du type **Blonde***

Les paramètres peuvent se combiner pour faire une rechercehe de bière plus précises

Pour récupérer des suggestion de 10 bières du moment, envoyez une requête GET à l'endpoit ```/recommandations```
```bash
curl http://127.0.0.1:2711/recommandations
```
> *Cette requête retournera une suggestion de 10 bières du moment.*



### Réponse de l'API

La réponse sera au format JSON. Par exemple :

```json
[
    {
        "Name": "Duvel",
        "ABV": 8.5,
        "Type": "Blonde Forte",
        "Brewery": "Duvel Moortgat",
        "Description": "Une Ale forte belge qui offre un mélange complexe d'arômes floraux de houblon et de douceur maltée équilibrée.",
        "Image_URL" : "https://www.amstein.ch/Htdocs/Images/Pictures/101571.jpg"
    },
    {
        "Name": "Tripel Karmeliet",
        "ABV": 8.4,
        "Type": "Tripel",
        "Brewery": "Brouwerij Bosteels",
        "Description": "Une Tripel belge raffinée et complexe brassée avec trois types de grains et un profil de saveur robuste.",
        "Image_URL": "https://www.amstein.ch/Htdocs/Images/IF_Bottle_700/111911.jpg"
    }
]
```

## Docker

Pour build le container, il faut lancer lac ommande suivante :
```bash
docker build -t api_beers .
```

Pour monter le container
```bash
docker run -d -name api_beers -p 2711:2711 api_beers
```

### Erreurs

- **404 Non Trouvé :** Si aucune bière ne répond aux critères d'ABV spécifiés.
- **500 Erreur Interne du Serveur :** S'il y a un problème de chargement des données sur les bières.