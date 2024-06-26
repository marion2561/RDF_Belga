from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)

# Configuration de CORS pour autoriser l'origine du client7
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Créer un Blueprint avec un préfixe de base pour toutes les routes
beer_services = Blueprint('beer_services', __name__)

# Charger les données des bières
def load_beers_data():
    try:
        data = pd.read_csv("./beers.csv")
        return data
    except Exception as e:
        print(f"Error loading beer data: {e}")
        return None
    
# Route pour obtenir une recommandation de 10 bières
@beer_services.route('/recommandations', methods=['GET'])
def recommandations():
    beers = load_beers_data()
    if beers is None or beers.empty:
        return jsonify({"error": "Beer data could not be loaded or is empty"}), 500
    else:
        recommandations_beers = beers.sample(10).to_dict(orient="records")
        return jsonify(recommandations_beers), 200

# Route pour obtenir des bières selon le type et/ou un ABV minimum spécifié
@beer_services.route('/beers', methods=['GET'])
def get_beers():
    min_abv = request.args.get('min_abv', type=float)
    beer_type = request.args.get('type', type=str)
    id_beer = request.args.get('id', type=int)
    
    beers = load_beers_data()
    if beers is None or beers.empty:
        return jsonify({"error": "Beer data could not be loaded or is empty"}), 500

    if min_abv is not None:
        beers = beers[beers['ABV'] >= min_abv]

    if beer_type:
        beers = beers[beers['Type'].str.lower() == beer_type.lower()]

    if id_beer:
        beers = beers[beers['Id'] == id_beer]

    filtered_beers = beers.to_dict(orient='records')
    if filtered_beers:
        return jsonify(filtered_beers), 200
    else:
        return jsonify({"message": "No beers found matching the criteria"}), 404

# Enregistrer le Blueprint dans l'application Flask
app.register_blueprint(beer_services)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2711)
