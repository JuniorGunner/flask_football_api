from app import db


class Competition(db.Model):
    __tablename__ = 'competition'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    areaName = db.Column(db.String(100), nullable=False)

    teams = db.relationship('Team', backref='competition', lazy=True)

    def __repr__(self):
        return f"Competition('{self.name}', '{self.code}')"
