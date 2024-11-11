from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from player_reader import PlayerReader
from player_stats import PlayerStats
from player import Player



def main():
    season = Prompt.ask("Select season", choices=["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"])
    reader = PlayerReader(season)
    stats = PlayerStats(reader)

    console = Console()

    while True:


        nationality = Prompt.ask(
            "Select nationality", 
            choices=["AUT", "CZE", "AUS", "SWE", "GER", "DEN", "SUI", "SVK", "NOR", "RUS", "CAN", "LAT", "BLR", "SLO", "USA", "FIN", "GBR", "quit"]
            )

        if nationality == 'quit':
            break

        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title="NHL statistics by nationality")
        table.add_column("name")
        table.add_column("team")
        table.add_column("goals")
        table.add_column("assists")
        table.add_column("points")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals+player.assists))

        console.print(table)


if __name__ == "__main__":
    main()
