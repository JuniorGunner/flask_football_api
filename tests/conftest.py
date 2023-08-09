import pytest
from app import create_app, db
from models.competition import Competition
from models.team import Team
from models.player import Player
from models.coach import Coach

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory SQLite for tests

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        db.session.remove()
        db.drop_all()

@pytest.fixture
def sample_data():
    competition = Competition(name='Premier League', code='PL', areaName='England')
    team = Team(name='TeamName', tla='TN', shortName='Team', areaName='England', address='Some address', competition=competition)
    player = Player(name='PlayerName1', position='Midfielder', dateOfBirth='1990-01-01', nationality='English', team=team)
    coach = Coach(name='CoachName', dateOfBirth='1970-01-01', nationality='English', team=team)

    db.session.add(competition)
    db.session.add(team)
    db.session.add(player)
    db.session.add(coach)
    db.session.commit()

    return competition, team, player, coach

@pytest.fixture
def mock_football_api(monkeypatch):
    """ Mock the http://www.football-data.org/ API """

    def mock_get(*args, **kwargs):
        class MockResponse:
            @staticmethod
            def json():
                return {
                    "competitions": [{"name": "Premier League", "code": "PL", "area": {"name": "England"}}],
                    "teams": [{"name": "TeamName", "tla": "TN", "shortName": "Team", "area": {"name": "England"}, "address": "Some address"}],
                    "players": [{"name": "PlayerName1", "position": "Midfielder", "dateOfBirth": "1990-01-01", "nationality": "English"}],
                    "coaches": [{"name": "CoachName", "dateOfBirth": "1970-01-01", "nationality": "English"}]
                }

        monkeypatch.setattr("requests.get", mock_get)
