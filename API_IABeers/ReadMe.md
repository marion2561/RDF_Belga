
# API Orders

## Description
API Orders est une application FastAPI conçue pour gérer les commandes et leurs lignes d'articles. Elle permet d'importer, traiter et accéder à des informations de commandes via une interface API.

## Installation

Pour installer les dépendances nécessaires, exécutez :

```bash
pip freeze > requirements.txt
```

## Démarrage de l'application

Pour démarrer le serveur FastAPI, exécutez :

```bash
uvicorn app.main:app --reload
```

Cela lancera l'application sur `localhost` avec le port `80`.

## Utilisation

### Endpoints disponibles

- `GET /orders`: Retourne une liste de toutes les commandes.
- `POST /orders`: Ajoute une nouvelle commande.
- `GET /orders/{order_id}`: Retourne les détails d'une commande spécifique.

## Structure du projet

- **main.py** : Point d'entrée de l'application FastAPI.
- **Order.py** : Modèles pour les objets Commande.
- **OrderLine.py** : Modèles pour les objets Ligne de Commande.
- **FileReaderUtil.py** : Utilitaire pour lire les fichiers.
- **Files** : Dossier contenant les fichiers nécessaires.

## Configuration Docker

Pour containeriser l'application FastAPI avec Docker, suivez ces étapes :

1. Construisez l'image Docker à partir du Dockerfile :
   ```bash
   docker build -t api_iabeers .
      docker build --no-cache -t api_iabeers .
   ```

2. Une fois l'image construite, vous pouvez démarrer le conteneur :
   ```bash
   docker run --network rdf_network -d --name api_iabeers -p 89:89 api_iabeers
   ```

Cela démarrera l'application dans un conteneur Docker, accessible via `localhost:85`.
