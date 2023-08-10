class Team:
    def __init__(self, name, tla, short_name, area_name, address=None, competition_id=None, players=[], coaches=[]):
        self.name = name
        self.tla = tla
        self.short_name = short_name
        self.area_name = area_name
        self.address = address
        self.competition_id = competition_id
        self.players = players  # This can be a list of embedded Player documents or IDs.
        self.coaches = coaches  # This can be a list of embedded Coach documents or IDs.

    def __repr__(self):
        return f"Team('{self.name}', '{self.tla}')"
