class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict["team"]
        self.goals = dict["goals"]
        self.assists = dict["assists"]
        self.nationality = dict["nationality"]
        self.games = dict["games"]

    def __str__(self):
        return f"{self.name:20}{self.team:4}{self.goals:4} + {self.assists:2} = {self.goals + self.assists:2}"
