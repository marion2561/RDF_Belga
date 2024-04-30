from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)

# Configuration de CORS pour autoriser l'origine du client7
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Créer un Blueprint avec un préfixe de base pour toutes les routes
beer_services = Blueprint('beer_services', __name__, url_prefix='/beer_services')

# Charger les données des bières
def load_beers_data():
    try:
        data = pd.read_csv("./beer_services/beers.csv")
        return data
    except Exception as e:
        print(f"Error loading beer data: {e}")
        return None

# Route pour obtenir des bières selon le type et/ou un ABV minimum spécifié
@beer_services.route('/beers', methods=['GET'])
def get_beers():
    min_abv = request.args.get('min_abv', type=float)
    beer_type = request.args.get('type', type=str)
    
    beers = load_beers_data()
    if beers is None or beers.empty:
        return jsonify({"error": "Beer data could not be loaded or is empty"}), 500

    if min_abv is not None:
        beers = beers[beers['ABV'] >= min_abv]

    if beer_type:
        beers = beers[beers['Type'].str.lower() == beer_type.lower()]

    filtered_beers = beers.to_dict(orient='records')
    if filtered_beers:
        return jsonify(filtered_beers), 200
    else:
        return jsonify({"message": "No beers found matching the criteria"}), 404

# Enregistrer le Blueprint dans l'application Flask
app.register_blueprint(beer_services)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
