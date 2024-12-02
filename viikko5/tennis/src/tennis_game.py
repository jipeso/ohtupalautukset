class TennisGame:
    POINTS = ["Love", "Fifteen", "Thirty", "Forty"]
    DEUCEMAKER = 3
    WIN_MARGIN = 2

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.scores = {player1 : 0, player2 : 0}

    def won_point(self, player):
        self.scores[player] += 1

    def get_score(self):
        if self.scores[self.player1] == self.scores[self.player2]:
            return self.even_score()

        return self.check_winner()

    def even_score(self):
        points = self.scores[self.player1]

        if points < self.DEUCEMAKER:
            return f"{self.POINTS[points]}-All"

        return "Deuce"

    def check_winner(self):
        p1_points = self.scores[self.player1]
        p2_points = self.scores[self.player2]

        if p1_points > self.DEUCEMAKER or p2_points > self.DEUCEMAKER:
            if abs(p1_points - p2_points) >= self.WIN_MARGIN:
                return f"Win for {self.player1}" if p1_points > p2_points else f"Win for {self.player2}"
            
            return f"Advantage {self.player1}" if p1_points > p2_points else f"Advantage {self.player2}"
        
        return f"{self.POINTS[p1_points]}-{self.POINTS[p2_points]}"
