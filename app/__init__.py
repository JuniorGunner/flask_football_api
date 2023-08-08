from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

# Extensions are initialized here without binding to the app.
db = SQLAlchemy()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    from app.routes.main import main
    app.register_blueprint(main)

    return app
