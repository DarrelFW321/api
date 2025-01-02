from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests
        
@app.route('/', methods=['GET'])
def lebron_stats():
    career = playercareerstats.PlayerCareerStats(player_id=2544)
    data = career.get_dict()

    # Get career total points
    regular_season_career = data['resultSets'][1]
    regular_season_points = regular_season_career['rowSet'][0][23]  # Points
    postseason_career = data['resultSets'][3]
    postseason_points = postseason_career['rowSet'][0][23]

    return jsonify({
        "player": "LeBron James",
        "career_points": regular_season_points + postseason_points
    })

if __name__ == '__main__':
    app.run(debug=True)