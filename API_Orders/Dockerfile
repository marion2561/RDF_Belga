# Utilisation de l'image de base Python 3.9
FROM python:3.9

# Définition du répertoire de travail dans le conteneur
WORKDIR /code

# Copie du fichier requirements.txt dans le répertoire de travail
COPY ./requirements.txt /code/requirements.txt

# Installation des dépendances à partir du fichier requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copie du dossier app dans le répertoire de travail
COPY ./app /code/app

# Exposition du port 80
EXPOSE 85

# Commande pour démarrer l'application avec Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "85"]
