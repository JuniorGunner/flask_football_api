from flask import Blueprint, jsonify
from app import mongo

players_blueprint = Blueprint('players', __name__)

@players_blueprint.route('/players/<leagueCode>', methods=['GET'])
def get_players(leagueCode):
    competition = mongo.db.competitions.find_one({"code": leagueCode})

    if not competition:
        return jsonify({"message": "Competition not found"}), 404

    teams = list(mongo.db.teams.find({"competition_id": competition["_id"]}))
    player_names = []
    for team in teams:
        players = list(mongo.db.players.find({"team_id": team["_id"]}))
        player_names.extend([player["name"] for player in players])

    return jsonify(player_names)


@players_blueprint.route('/players-of-team/<teamName>', methods=['GET'])
def get_players_of_team(teamName):
    team = mongo.db.teams.find_one({"name": teamName})

    if not team:
        return jsonify({"message": "Team not found"}), 404

    players = list(mongo.db.players.find({"team_id": team["_id"]}))
    return jsonify([player["name"] for player in players])
