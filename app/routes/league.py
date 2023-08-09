from flask import Blueprint, jsonify
import requests
from app import db
from ..models.competition import Competition
from ..models.team import Team
from ..models.player import Player
from ..models.coach import Coach

league_blueprint = Blueprint('league', __name__)

# Set the API token and base URL
API_TOKEN = 'YOUR_API_TOKEN'
HEADERS = {
    'X-Auth-Token': API_TOKEN
}
BASE_URL = "https://api.football-data.org/v4/competitions/"


@league_blueprint.route('/import-league/<leagueCode>', methods=['GET'])
def import_league(leagueCode):
    """Endpoint to import data of a league using its league code.

    Parameters:
        leagueCode (str): The code of the league to be imported.

    Returns:
        dict: A message confirming that the league data was imported.
    """

     # Fetch league data
    league_url = f'{BASE_URL}{leagueCode}'
    league_response = requests.get(league_url, headers=HEADERS)
    league_data = league_response.json()

    # Import Competition
    competition = Competition(
        id=league_data["id"],
        name=league_data["name"],
        code=league_data["code"],
        areaName=league_data["area"]["name"]
    )
    db.session.add(competition)

    # Fetch teams data
    teams_url = f'{BASE_URL}{leagueCode}/teams'
    teams_response = requests.get(teams_url, headers=HEADERS)
    teams_data = teams_response.json()["teams"]

    # Import Teams
    for team_data in teams_data:
        team = Team(
            id=team_data["id"],
            name=team_data["name"],
            tla=team_data["tla"],
            shortName=team_data["shortName"],
            areaName=team_data["area"]["name"],
            address=team_data.get("address", None),
            competition_id=competition.id
        )
        db.session.add(team)

        # Import Coach
        coach_data = team_data.get("coach", {})  # some teams might not have a coach listed
        if coach_data:
            coach = Coach(
                id=coach_data.get("id", None),
                name=coach_data.get("name", ""),
                dateOfBirth=coach_data.get("dateOfBirth", None),
                nationality=coach_data.get("nationality", None),
                team_id=team.id
            )
            db.session.add(coach)

        # Import Players
        for player_data in team_data.get("squad", []):
            player = Player(
                id=player_data["id"],
                name=player_data["name"],
                position=player_data.get("position", None),
                dateOfBirth=player_data.get("dateOfBirth", None),
                nationality=player_data.get("nationality", None),
                team_id=team.id
            )
            db.session.add(player)

    db.session.commit()

    return jsonify({"message": "Imported league data for league code: " + leagueCode})
