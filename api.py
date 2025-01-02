from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

@app.route('/api/lebron_stats', methods=['GET'])
def lebron_stats():
    # Fetch LeBron James' stats
    player = players.find_players_by_full_name('LeBron James')[0]
    player_id = player['id']
    
    timeout = Timeout(60)  # Increase timeout to 60 seconds

    career = playercareerstats.PlayerCareerStats(player_id=player_id, timeout = timeout)
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
