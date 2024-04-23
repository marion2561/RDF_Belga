# API des plats de Bélga
L'API des plats de Bélga offre un service web simple pour récupérer une liste de plats. Elle est construite en utilisant [Laravel](https://laravel.com/), un framework web léger pour PHP, et utilise [league/csv]() qui traiter les données CSV.
## Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :
- PHP (version 8.2 ou supérieure)
- Composer
- Serveur web (Apache, Nginx, etc.)
- Git
## Installation
1. Clonez ce référentiel sur votre machine locale :
```.sh
git clone https://github.com/marion2561/RDF_Belga.git
```
2. Accédez au répertoire du projet :
```.sh
cd RDF_BELGA/plats
```
3. Installez les dépendances PHP via Composer :
```.sh
composer install
```
4. Copiez le fichier .env.example et renommez-le en .env :
```.sh
cp .env.example .env
```
5. Générez une nouvelle clé d'application Laravel :
```.sh
php artisan key:generate
```

6. Configurez votre base de données dans le fichier `.env`, ou utilisez un fichier CSV pour les données, cette étape n'est pas nécessaire.

7. Assurez-vous que le fichier CSV contenant les données des plats est présent dans le chemin suivant : `plats/storage/app/plats/plats.csv`.

8. Démarrez le serveur de développement Laravel : 
```.php
php artisan serve
```
Par défaut, le serveur devrait démarrer sur http://localhost:8000.

## Utilisation
Une fois le serveur lancé, vous pouvez accéder aux services exposés par l'API pour la gestion des plats du restaurant belge. Voici les points d'accès disponibles :

- `GET /api/plats`: Récupère la liste de tous les plats disponibles.
- `GET /api/plats/{id}`: Récupère un plat spécifique en fonction de son ID.
`POST /api/plats`: Crée un nouveau plat.
`PUT /api/plats/{id}`: Met à jour un plat existant.
`DELETE /api/plats/{id}`: Supprime un plat existant.
Assurez-vous de remplacer `localhost:8000` par l'URL de votre serveur si vous utilisez une adresse différente.

## Auteurs
- [Hazahr Galeh](https://github.com/hazhargaleh)