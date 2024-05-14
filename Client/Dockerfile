# Utilisation de l'image Nginx officielle
FROM nginx:latest

# Mise à jour et installation des dépendances
RUN apt update && apt install -y

# Copie des fichiers du dossier Client dans le répertoire de travail de Nginx
COPY . /usr/share/nginx/html

# Exposition du port 80
EXPOSE 80

# Commande pour démarrer Nginx
CMD ["nginx", "-g", "daemon off;"]
