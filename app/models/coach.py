class Coach:
    def __init__(self, name, date_of_birth=None, nationality=None, team_id=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.nationality = nationality
        self.team_id = team_id

    def __repr__(self):
        return f"Coach('{self.name}')"
