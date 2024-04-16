from flask import Flask, jsonify, request
import pandas as pd
import random

app = Flask(__name__)

# Charger les données des bières
def load_beers_data():
    try:
        data = pd.read_csv("beers.csv")
        return data
    except Exception as e:
        print(f"Error loading beer data: {e}")
        return None

# Route pour obtenir les bières avec un ABV minimum spécifié
@app.route('/beers', methods=['GET'])
def beers_by_abv():
    min_abv = request.args.get('min_abv', type=float)
    if min_abv is None:
        return jsonify({"error": "Missing 'min_abv' query parameter"}), 400

    beers = load_beers_data()
    if beers is not None and not beers.empty:
        filtered_beers = beers[beers['ABV'] >= min_abv].to_dict(orient="records")
        if filtered_beers:
            return jsonify(filtered_beers), 200
        else:
            return jsonify({"message": "No beers found with ABV greater than or equal to {}".format(min_abv)}), 404
    else:
        return jsonify({"error": "Beer data could not be loaded or is empty"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
