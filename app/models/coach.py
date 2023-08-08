from app import db


class Coach(db.Model):
    __tablename__ = 'coach'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dateOfBirth = db.Column(db.Date, nullable=True)
    nationality = db.Column(db.String(100), nullable=True)

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    def __repr__(self):
        return f"Coach('{self.name}')"
