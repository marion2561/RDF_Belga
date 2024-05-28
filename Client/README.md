# BELGA - Site Web client

## Structure du Projet

Le projet est structuré en plusieurs pages HTML et fichiers JavaScript associés pour gérer les différentes fonctionnalités du site. Voici une description des différentes pages et de leurs fonctions.

### Page d'accueil

1. **index.html**
     - Affiche le plat du jour avec une bière sélectionnée.
     - Utilise un spinner pour indiquer le chargement des données.
     - Affiche les détails de la bière et du plat sélectionné une fois les données chargées.
2. **index.js**
     - Gère le chargement des données pour la page d'accueil.
     - Affiche les informations du plat et de la bière du jour.
     - Gère les erreurs de chargement et les tentatives de rechargement.

### Page bières
1. **bieres.html**
     - Filtrage des bières par taux d'alcool (ABV) minimum.
     - Filtrage des bières par type.
     - Recherche de bières par nom.
     - Affichage des bières sous forme de cartes avec des détails comme l'image, le nom, le type, la brasserie, le taux d'alcool et une description.
2. **bieres.js**
     - Récupère les données des bières depuis une API.
     - Remplit les cartes des bières et les filtres de sélection (type de bière).
     - Gère les filtres par taux d'alcool, type de bière et recherche par nom.

### Page plats
1. **plats.html**
     - Affichage des plats sous forme de cartes avec des détails comme l'image, le nom, le prix, les ingrédients, la popularité et une description.
     - Affichage de la popularité sous forme d'étoiles.
     - Ouverture d'une modal pour afficher les bières recommandées pour un plat sélectionné.
2. **plats.js**
     - Récupère les données des plats depuis une API.
     - Remplit les cartes des plats avec des informations détaillées.
     - Ouvre une modal pour afficher les bières recommandées pour un plat spécifique.
     - Affiche la popularité des plats sous forme d'étoiles.
### Page commandes

1. **commandes.html**
     - Affichage d'un tableau des commandes avec des détails comme le numéro de commande, le client, la date et le prix.
     - Affichage des détails de chaque commande en cliquant sur une ligne du tableau.

2. **commandes.js**
   - **Fonctionnalités** :
     - Récupère les données des commandes depuis une API.
     - Remplit le tableau des commandes avec des informations détaillées.
     - Affiche les détails des commandes en cliquant sur les lignes du tableau.

### Dépendances
- Bootstrap 5 pour la mise en page et le style.
- Services connexes qui doivent être éxécutés en parrallèle.

