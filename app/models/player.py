class Player:
    def __init__(self, name, position=None, date_of_birth=None, nationality=None, team_id=None):
        self.name = name
        self.position = position
        self.date_of_birth = date_of_birth
        self.nationality = nationality
        self.team_id = team_id

    def __repr__(self):
        return f"Player('{self.name}', '{self.position}')"
