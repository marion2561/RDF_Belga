# Utiliser une image de base officielle Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application dans le répertoire de travail
COPY . .

# Exposer le port sur lequel le serveur Flask s'exécutera
EXPOSE 2711

# Définir la commande pour lancer l'application
CMD ["python", "beer_services.py"]
