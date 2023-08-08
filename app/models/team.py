from app import db


class Team(db.Model):
    __tablename__ = 'team'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tla = db.Column(db.String(10), nullable=False)
    shortName = db.Column(db.String(100), nullable=False)
    areaName = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=True)

    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    
    players = db.relationship('Player', backref='team', lazy=True)
    coaches = db.relationship('Coach', backref='team', lazy=True)

    def __repr__(self):
        return f"Team('{self.name}', '{self.tla}')"
