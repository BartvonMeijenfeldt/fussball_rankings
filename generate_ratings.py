import csv
from datetime import datetime
from src.barto.rating_result import RatingResult

from src.barto.barto import BartoRatings
from src.barto.game_result import GameResult
from src.barto.ratings import Player


def read_game_results(path: str) -> list[GameResult]:
    with open(path, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=';')
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


def get_ratings_and_results(game_results: list[GameResult]) -> tuple[list[Player], list[RatingResult]]:
    barto_ratings = BartoRatings(init_rating=1500, sd_rating=100, sd_game_performance=100)
    barto_ratings.add_results(results=game_results)
    return barto_ratings.ratings, barto_ratings.rating_results


def save_ratings(ratings: list[Player]) -> None:
    filename = _get_file_name('beta_ratings')
    ratings.sort(reverse=True)

    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=',')

        header = ['Player', 'Rating', '#Games']
        writer.writerow(header)

        for player in ratings:
            values = [player.name, player.rating, player.nr_games]
            writer.writerow(values)


def save_rating_results(rating_results: list[RatingResult]) -> None:
    filename = _get_file_name('beta_rating_results')

    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=',')

        header = ['Team1', 'Team2', 'PointsTeam1', 'PointsTeam2', 'RatingAdvantage',
                  'ExpectedPercentScore', 'AchievedPercentScore', 'RatingGainPlayersTeam1']
        writer.writerow(header)

        for result in rating_results:
            values = [', '.join(result.team1), ', '.join(result.team2),
                      result.points_team1, result.points_team2,
                      round(result.rating_advantage, ndigits=1),
                      round(result.expected_percent_score, ndigits=3),
                      round(result.achieved_percent_score, ndigits=3),
                      result.rating_gain_players_team1]
            writer.writerow(values)


def _get_file_name(base_name: str) -> str:
    now_str = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M')
    filename = f'{base_name}_{now_str}.csv'
    return filename

if __name__ == "__main__":
    game_results = read_game_results('results_table_football.csv')
    ratings, rating_results = get_ratings_and_results(game_results=game_results)
    save_ratings(ratings=ratings)
    save_rating_results(rating_results=rating_results)
