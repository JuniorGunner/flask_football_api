from app import db


class Player(db.Model):
    __tablename__ = 'player'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50), nullable=True)
    dateOfBirth = db.Column(db.Date, nullable=True)
    nationality = db.Column(db.String(100), nullable=True)

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    def __repr__(self):
        return f"Player('{self.name}', '{self.position}')"
