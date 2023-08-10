from flask import Blueprint, jsonify
from app import mongo

team_blueprint = Blueprint('team', __name__)

@team_blueprint.route('/team/<teamName>', methods=['GET'])
def get_team(teamName):
    team = mongo.db.teams.find_one({"name": teamName})

    if not team:
        return jsonify({"message": "Team not found"}), 404

    return jsonify({
        "name": team["name"],
        "tla": team["tla"],
        "shortName": team["shortName"],
        "areaName": team["area"]["name"],
        "address": team.get("address", "")
    })
