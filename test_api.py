from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

@app.route('/test_api', methods=['GET'])
def test_api():
    try:
        # Try to make a request to the NBA stats API
        response = requests.get('https://stats.nba.com/stats/playercareerstats', timeout=30)
        response.raise_for_status()  # Raise an exception for bad responses
        return jsonify({"status": "success", "data": response.json()})
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "error", "error": str(e)}), 500
