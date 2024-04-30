# Utilisation de l'image de base Python 3.9
FROM python:3.9

# Définition du répertoire de travail dans le conteneur
WORKDIR /code

# Copie du fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installation des dépendances à partir du fichier requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copie du reste du projet dans le répertoire de travail
COPY . .

# Exposition du port sur lequel votre application s'exécute
EXPOSE 81

# Commande pour démarrer votre application, ajustez le chemin selon l'emplacement de app.py
CMD ["python", "app/app.py"]