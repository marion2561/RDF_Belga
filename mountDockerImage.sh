#!/bin/bash

# Fonction pour créer une image Docker pour un projet
creer_image() {
    nom_projet=$1
    chemin_projet=$2
    tag=$3

    # Se déplacer dans le dossier du projet
    cd $chemin_projet

    # Construire l'image Docker
    docker build -t $nom_projet:$tag .

    # Revenir au dossier parent
    cd -
}

# Fonction pour créer un conteneur à partir d'une image
creer_ou_recreer_conteneur() {
    nom_image=$1
    nom_conteneur=$2
    portmap_pc=$3
    portmap_docker=$4

    # Vérifier si le conteneur existe
    if [ "$(docker ps -aq -f name=$nom_conteneur)" ]; then
        # Si le conteneur existe, le supprimer
        docker rm -f $nom_conteneur
    fi

    # Créer le conteneur à partir de l'image spécifiée
    docker run --network rdf_network -d --name $nom_conteneur -p $portmap_pc:$portmap_docker -d $nom_image
}

docker network create rdf_network

# Projet 1
echo "Création de l'image pour le projet API_Orders"
creer_image "api_orders" "API_Orders" "latest"
creer_ou_recreer_conteneur "api_orders:latest" "api_orders" "85" "85"

# Projet 2
echo "Création de l'image pour le projet API_Beers"
creer_image "api_beers" "API_Beers" "latest"
creer_ou_recreer_conteneur "api_beers:latest" "api_beers" "2711" "2711"

# Projet 3
echo "Création de l'image pour le projet API_Plats"
creer_image "api_plats" "API_plats" "latest"
creer_ou_recreer_conteneur "api_plats:latest" "api_plats" "8000" "80"

# Projet 4
echo "Création de l'image pour le projet API_Gateway"
creer_image "api_gateway" "API_Gateway" "latest"
creer_ou_recreer_conteneur "api_gateway:latest" "api_gateway" "81" "81"

# Créer les conteneurs
# Vous pouvez ajouter ici des commandes pour démarrer les conteneurs avec les images fraîchement créées
