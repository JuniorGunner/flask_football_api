from flask import Blueprint, request, jsonify
from ..models.competition import Competition
from ..models.team import Team
from ..models.player import Player
from ..models.coach import Coach
from app import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return "Hello, World!"


@main.route('/import-league/<leagueCode>', methods=['GET'])
def import_league(leagueCode):
    # Call the Football-data.org API here to get data
    # and save it to SQLite database.

    return jsonify({"message": "Imported league data for league code: " + leagueCode})


@main.route('/players/<leagueCode>', methods=['GET'])
def get_players(leagueCode):
    # Assuming leagueCode maps to the 'code' in the Competition model
    competition = Competition.query.filter_by(code=leagueCode).first()

    if not competition:
        return jsonify({"message": "Competition not found"}), 404

    # Fetch players of all teams in the competition
    teams = Team.query.filter_by(competition_id=competition.id).all()
    players = [player for team in teams for player in team.players]

    return jsonify([player.name for player in players])


@main.route('/team/<teamName>', methods=['GET'])
def get_team(teamName):
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


@main.route('/players-of-team/<teamName>', methods=['GET'])
def get_players_of_team(teamName):
    team = Team.query.filter_by(name=teamName).first()

    if not team:
        return jsonify({"message": "Team not found"}), 404

    return jsonify([player.name for player in team.players])
