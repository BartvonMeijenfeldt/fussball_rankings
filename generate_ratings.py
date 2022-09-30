import csv

from src.barto.game_calculation import GameCalculation
from src.barto.barto import BartoRatings
from src.barto.game_result import GameResult
from src.barto.ratings import Player


def read_game_results(path: str) -> list[GameResult]:
    with open(path, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        game_results = [_convert_row_to_single_game_result(header, row) for row in reader]

    return game_results


def _convert_row_to_single_game_result(header: list[str], row: list[str]) -> GameResult:
    row_dict = dict(zip(header, row))

    team1 = [player for col_name, player in row_dict.items() if col_name.startswith('Team 1')]
    team2 = [player for col_name, player in row_dict.items() if col_name.startswith('Team 2')]
    points_team1 = int(row_dict['Score Team 1'])
    points_team2 = int(row_dict['Score Team 2'])
    return GameResult(team1=team1, team2=team2, points_team1=points_team1, points_team2=points_team2)


def get_ratings_and_calculations(game_results: list[GameResult]) -> tuple[list[Player], list[GameCalculation]]:
    barto_ratings = BartoRatings(init_rating=1500, sd_rating=100, sd_game_performance=100)
    barto_ratings.add_results(results=game_results)
    return barto_ratings.ratings, barto_ratings.calculations


def save_ratings(ratings: list[Player]) -> None:
    filename = 'beta_ratings.csv'
    ratings.sort(reverse=True)

    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=',')

        header = ['Player', 'Rating', '#Games']
        writer.writerow(header)

        for player in ratings:
            values = [player.name, player.rating, player.nr_games]
            writer.writerow(values)


def save_calculations(calculations: list[GameCalculation]) -> None:
    filename = 'calculations.csv'

    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=',')

        header = ['Team1', 'Team2', 'PointsTeam1', 'PointsTeam2', 'RatingAdvantage',
                  'ExpectedPercentScore', 'AchievedPercentScore', 'RatingGainPlayersTeam1']
        writer.writerow(header)

        for result in calculations:
            values = [', '.join(result.team1), ', '.join(result.team2),
                      result.points_team1, result.points_team2,
                      round(result.rating_advantage, ndigits=1),
                      round(result.expected_percent_score, ndigits=3),
                      round(result.achieved_percent_score, ndigits=3),
                      result.rating_gain_players_team1]
            writer.writerow(values)


if __name__ == "__main__":
    game_results = read_game_results('results_table_football.csv')
    ratings, calculations = get_ratings_and_calculations(game_results=game_results)
    save_ratings(ratings=ratings)
    save_calculations(calculations=calculations)
