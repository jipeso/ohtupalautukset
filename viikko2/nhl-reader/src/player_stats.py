from player import Player

class PlayerStats:
    def __init__(self, player_reader):
        self.reader = player_reader
        self.players = self.reader.get_players()

    def top_scorers_by_nationality(self, nationality):
            players_from_nationality = []

            for player in self.players:
                 if player.nationality == nationality:
                      players_from_nationality.append(player)

            return sorted(players_from_nationality, key=lambda player: player.goals + player.assists, reverse=True)
