from flask import Flask
from config import config
from flask_pymongo import PyMongo  # Using Flask-PyMongo as a bridge

mongo = PyMongo()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    mongo.init_app(app)

    # Register blueprints
    from app.routes.index import index_blueprint
    from app.routes.league import league_blueprint
    from app.routes.players import players_blueprint
    from app.routes.team import team_blueprint

    app.register_blueprint(index_blueprint)
    app.register_blueprint(league_blueprint)
    app.register_blueprint(players_blueprint)
    app.register_blueprint(team_blueprint)

    return app
