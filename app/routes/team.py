from flask import Blueprint, jsonify
from ..models.team import Team

team_blueprint = Blueprint('team', __name__)

@team_blueprint.route('/team/<teamName>', methods=['GET'])
def get_team(teamName):
    """Endpoint to fetch details of a team by its name.

    Parameters:
        teamName (str): The name of the team to be fetched.

    Returns:
        dict: Team details or error message if teamName is not found.
    """

    team = Team.query.filter_by(name=teamName).first()

    if not team:
        return jsonify({"message": "Team not found"}), 404

    return jsonify({
        "name": team.name,
        "tla": team.tla,
        "shortName": team.shortName,
        "areaName": team.areaName,
        "address": team.address
    })
