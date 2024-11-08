import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
    
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 37)
        self.assertEqual(player.assists, 53)
        self.assertEqual(player.points, 90)
        self.assertEqual(str(player), "Kurri EDM 37 + 53 = 90")


    def test_search_nonexistent_player(self):
        player = self.stats.search("Litmanen")

        self.assertEqual(player, None)

    def test_search_team_players(self):
        team = self.stats.team("PIT")

        self.assertEqual(len(team), 1)

    def test_search_nonexistent_team_players(self):
        team = self.stats.team("Jokerit")

        self.assertEqual(len(team), 0)

    def test_find_top_players(self):
        players = self.stats.top(2)

        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Gretzky")
    
        players = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(players[0].name, "Gretzky")

        players = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(players[0].name, "Lemieux")

        players = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(players[0].name, "Gretzky")
