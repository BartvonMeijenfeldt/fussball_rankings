import csv
from datetime import date
from operator import itemgetter

from src.barto.barto import BartoRatings
from src.barto.game_result import GameResult


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


def get_ratings(game_results: list[GameResult]) -> dict:
    barto_ratings = BartoRatings(init_rating=1500, sd_rating=100, sd_game_performance=100)
    barto_ratings.add_results(results=game_results)
    return barto_ratings.ratings


def save_results(ratings: dict) -> None:
    filename = f'ratings_{date.today()}.csv'
    rating_list = list(ratings.items())
    rating_list.sort(key=itemgetter(1), reverse=True)

    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        header = ['Player', 'Rating']
        writer.writerow(header)

        for row in rating_list:
            writer.writerow(row)

if __name__ == "__main__":
    game_results = read_game_results('results_table_football.csv')
    ratings = get_ratings(game_results=game_results)
    save_results(ratings=ratings)
