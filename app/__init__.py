from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config


# Extensions are initialized here without binding to the app.
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Model imports
    from .models.competition import Competition
    from .models.team import Team
    from .models.player import Player
    from .models.coach import Coach

    # Register blueprints
    from app.routes.main import main
    app.register_blueprint(main)

    return app
