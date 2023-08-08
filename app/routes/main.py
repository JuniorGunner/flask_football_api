from flask import Blueprint, request

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return "Hello, World!"


@main.route('/import-league/<leagueCode>', methods=['GET'])
def import_league(leagueCode):
    # Call the Football-data.org API using the league code
    # Parse the response and save the data to the SQLite database
    pass


@main.route('/players/<leagueCode>', methods=['GET'])
def get_players(leagueCode):
    # Query the SQLite database for the players of the teams in the given league
    pass


@main.route('/team/<teamName>', methods=['GET'])
def get_team(teamName):
    # Query the SQLite database for the team with the given name
    pass


@main.route('/players-of-team/<teamName>', methods=['GET'])
def get_players_of_team(teamName):
    # Query the SQLite database for the players of the team with the given name
    pass
