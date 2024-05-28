# Services de Belga

Ce projet propose plusieurs services pour gérer les bières, les plats et les commandes dans un restaurant.

## Services disponibles

- **API Beers** : Fournit une liste des bières enregistrées dans un fichier CSV.
- **API Plats** : Fournit une liste des plats enregistrés dans un fichier CSV.
- **API Orders** : Fournit une liste des commandes effectuées par les clients, enregistrées dans un fichier CSV.
- **API Gateway** : Cette API sert de passerelle entre les trois services ci-dessus, regroupant et retournant les résultats au client.
- **API IAMenu et API IABeers** : Proposent des menus de plats et de bières disponibles en fonction du stock.
- **Client** : Sert de l'affichage finale des services avec le lien http://localhost.

Dans le dossier de chacune des applications, vous trouverez un fichier README.md qui vous donne les instructions pour les lancer séparément.

Il faut garder en tête que le lancement des services `API Beers`, `API Plats` et `API Orders` est requis pour que `API Gateway`, `API IAMenu`, `API IABerrs` et `Client` fonctionnent.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Docker Engine : pour créer et exécuter des conteneurs Docker.
- Docker Compose : pour définir et exécuter des applications multi-conteneurs Docker.

**Systèmes d'exploitation pris en charge** : Linux, macOS, Windows
**Versions recommandées** :
- Docker Engine : 19.03.0 ou version ultérieure
- Docker Compose : 1.27.0 ou version ultérieure

## Installation via docker-compose

1. Clonez ce référentiel sur votre machine locale :

```
git clone https://github.com/marion2561/RDF_Belga.git
```


2. Accédez au répertoire du projet :

```
cd RDF_BELGA/
```


3. Utilisez la commande suivante pour créer et démarrer les conteneurs de chaque service :

```
docker-compose up
```

4. Par défaut, le serveur devrait démarrer sur le port 80 et vous pouvez accéder à l'interface client en suivant le lien ci-dessous :

    [http://localhost](http://localhost)

## Désinstallation

Assurez-vous d'avoir sauvegardé toutes les données importantes avant de procéder à la désinstallation complète.

Pour arrêter et supprimer complètement les conteneurs et les images Docker associées, utilisez la commande suivante :

```
docker compose down --rmi local
```

