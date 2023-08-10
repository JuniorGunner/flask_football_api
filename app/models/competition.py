class Competition:
    def __init__(self, name, code, area_name, teams=[]):
        self.name = name
        self.code = code
        self.area_name = area_name
        self.teams = teams  # This will be a list of embedded Team documents or IDs.

    def __repr__(self):
        return f"Competition('{self.name}', '{self.code}')"
