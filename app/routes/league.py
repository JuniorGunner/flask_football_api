import os
from flask import Blueprint, jsonify
import requests
from app import mongo
from requests.exceptions import RequestException

league_blueprint = Blueprint('league', __name__)

API_TOKEN = os.getenv("API_TOKEN")
HEADERS = {'X-Auth-Token': API_TOKEN}
BASE_URL = "https://api.football-data.org/v4/competitions/"


@league_blueprint.route('/import-league/<leagueCode>', methods=['GET'])
def import_league(leagueCode):
    try:
        # Fetch league data
        league_url = f'{BASE_URL}{leagueCode}'
        league_response = requests.get(league_url, headers=HEADERS)
        league_data = league_response.json()

        # Import Competition
        competitions = mongo.db.competitions
        competition_id = competitions.insert_one(league_data).inserted_id
        
        # Fetch teams data
        teams_url = f'{BASE_URL}{leagueCode}/teams'
        teams_response = requests.get(teams_url, headers=HEADERS)
        teams_data = teams_response.json()["teams"]

        # Import Teams, Coaches, and Players
        teams = mongo.db.teams
        for team_data in teams_data:
            team_data["competition_id"] = competition_id
            team_id = teams.insert_one(team_data).inserted_id
            
            # Store coaches and players in separate collections with references to the team they belong to
            if "coach" in team_data:
                coach_data = team_data.pop("coach")
                coach_data["team_id"] = team_id
                mongo.db.coaches.insert_one(coach_data)
            
            if "squad" in team_data:
                for player_data in team_data.pop("squad"):
                    player_data["team_id"] = team_id
                    mongo.db.players.insert_one(player_data)

        return jsonify({"message": f"Imported league data for league code: {leagueCode}"})

    except (RequestException, KeyError) as e:
        return jsonify({"error": str(e)}), 500
