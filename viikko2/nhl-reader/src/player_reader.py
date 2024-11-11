import requests
from player import Player


class PlayerReader:
    def __init__(self, season):
        self._season = season

    def get_players(self):
        url = f"https://studies.cs.helsinki.fi/nhlstats/{self._season}/players"
        response = requests.get(url).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

