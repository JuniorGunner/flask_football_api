from flask import Flask
import requests
from models import db, Player, Team, Competition

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.route('/import-league/<leagueCode>', methods=['GET'])
def import_league(leagueCode):
    # Call the Football-data.org API using the league code
    # Parse the response and save the data to the SQLite database
    pass

@app.route('/players/<leagueCode>', methods=['GET'])
def get_players(leagueCode):
    # Query the SQLite database for the players of the teams in the given league
    pass

@app.route('/team/<teamName>', methods=['GET'])
def get_team(teamName):
    # Query the SQLite database for the team with the given name
    pass

@app.route('/players-of-team/<teamName>', methods=['GET'])
def get_players_of_team(teamName):
    # Query the SQLite database for the players of the team with the given name
    pass

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
