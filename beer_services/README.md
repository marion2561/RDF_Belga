# API des Bières Belges

L'API des Bières Belges offre un service web simple pour récupérer une liste de bières belges filtrées par un pourcentage minimum d'alcool par volume (ABV). Elle est construite en utilisant Flask, un framework web léger pour Python, et utilise Pandas pour la gestion des données.

## Fonctionnalités

- **Obtenir des bières par ABV minimum** : Permet aux clients de demander des bières ayant un ABV supérieur ou égal à un minimum spécifié.

- **Obtenir une recommandation de 10 bières** : Permet aux clients de demander une suggestion de 10 bières du moment.

## Prérequis

Pour exécuter l'API, vous aurez besoin des éléments suivants :
- Python 3.6 ou supérieur
- Flask
- Pandas

Vous pouvez installer les bibliothèques nécessaires avec pip :

```bash
pip install flask pandas
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

3. **Exécution de l'API :**

Lancez l'application Flask en exécutant :

```bash
python beer_service.py
```

## Utilisation

Pour récupérer des bières par ABV minimum, envoyez une requête GET à l'endpoint ```/beers``` avec le paramètre de requête ```min_abv``` :
```bash
curl http://127.0.0.1:5000/beers?min_abv=8
```
*Cette requête retournera toutes les bières avec un ABV de 8% ou plus.*

Pour récupérer des suggestion de 10 bières du moment, envoyez une requête GET à l'endpoit ```/recommandations```
```bash
curl http://127.0.0.1:5000/recommandations
```
*Cette requête retournera une suggestion de 10 bièrs du moment.*



### Réponse de l'API

La réponse sera au format JSON. Par exemple :

```json
[
    {
        "Name": "Duvel",
        "ABV": 8.5,
        "Type": "Blonde Forte",
        "Brewery": "Duvel Moortgat",
        "Description": "Une Ale forte belge qui offre un mélange complexe d'arômes floraux de houblon et de douceur maltée équilibrée."
    },
    {
        "Name": "Tripel Karmeliet",
        "ABV": 8.4,
        "Type": "Tripel",
        "Brewery": "Brouwerij Bosteels",
        "Description": "Une Tripel belge raffinée et complexe brassée avec trois types de grains et un profil de saveur robuste."
    }
]
```

### Erreurs

- **400 Mauvaise Requête** : Si le paramètre ```min_abv``` est manquant.
- **404 Non Trouvé :** Si aucune bière ne répond aux critères d'ABV spécifiés.
- **500 Erreur Interne du Serveur :** S'il y a un problème de chargement des données sur les bières.