from flask import Blueprint, jsonify
from ..models.competition import Competition
from ..models.team import Team

players_blueprint = Blueprint('players', __name__)


@players_blueprint.route('/players/<leagueCode>', methods=['GET'])
def get_players(leagueCode):
    """Endpoint to fetch players of all teams in a given competition.

    Parameters:
        leagueCode (str): The code of the competition to fetch players from.

    Returns:
        list: A list of player names or error message if leagueCode is not found.
    """

    # Assuming leagueCode maps to the 'code' in the Competition model
    competition = Competition.query.filter_by(code=leagueCode).first()

    if not competition:
        return jsonify({"message": "Competition not found"}), 404

    # Fetch players of all teams in the competition
    teams = Team.query.filter_by(competition_id=competition.id).all()
    players = [player for team in teams for player in team.players]

    return jsonify([player.name for player in players])


@players_blueprint.route('/players-of-team/<teamName>', methods=['GET'])
def get_players_of_team(teamName):
    """Endpoint to fetch players of a team by its name.

    Parameters:
        teamName (str): The name of the team to fetch players from.

    Returns:
        list: A list of player names or error message if teamName is not found.
    """

    team = Team.query.filter_by(name=teamName).first()

    if not team:
        return jsonify({"message": "Team not found"}), 404

    return jsonify([player.name for player in team.players])
