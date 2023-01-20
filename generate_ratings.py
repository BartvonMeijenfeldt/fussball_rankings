import csv
import gspread

from barto.game_calculation import GameCalculation
from barto.barto import BartoRatings
from barto.game_result import GameResult
from barto.ratings import Player


def download_game_results(path: str) -> None:
    gc = gspread.service_account()
    game_results = gc.open('Fussball-Results-Transavia').get_worksheet(0).get_all_values()

    with open(path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(game_results)


def read_game_results(path: str) -> list[GameResult]:
    with open(path, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        game_results = [_convert_row_to_single_game_result(header, row) for row in reader]

    return game_results


def _convert_row_to_single_game_result(header: list[str], row_dict: list[str]) -> GameResult:
    row_dict = dict(zip(header, row_dict))

    team1 = _get_team(row_dict=row_dict, team_nr=1)
    team2 = _get_team(row_dict=row_dict, team_nr=2)

    points_team1 = int(row_dict['Score Team 1'])
    points_team2 = int(row_dict['Score Team 2'])

    return GameResult(team1=team1, team2=team2, points_team1=points_team1, points_team2=points_team2)


def _get_team(row_dict: dict, team_nr: int) -> tuple[str]:
    defense_player = row_dict[f'Team {team_nr} Defense'] + ' Defense'
    offense_player = row_dict[f'Team {team_nr} Offense'] + ' Offense'
    return defense_player, offense_player


def get_ratings_and_calculations(game_results: list[GameResult]) -> tuple[list[Player], list[GameCalculation]]:
    barto_ratings = BartoRatings(init_rating=1500, sd_rating=100, sd_game_performance=100)
    barto_ratings.add_results(results=game_results)
    return barto_ratings.ratings, barto_ratings.calculations


def add_avg_ratings(ratings: list[Player]) -> list[Player]:
    player_names = {player.name.rsplit(' ')[0] for player in ratings}
    player_lookups = {player.name: player for player in ratings}

    avg_ratings = [
        _create_all_games_player(player_name=player_name, player_lookups=player_lookups)
        for player_name in player_names
        if _player_has_offense_and_defense_rating(player_name=player_name, player_lookups=player_lookups)
    ]

    return ratings + avg_ratings


def _create_all_games_player(player_name: str, player_lookups: dict) -> Player:
    defense_player = player_lookups[_get_offense_name(player_name=player_name)]
    offense_player = player_lookups[_get_defense_name(player_name=player_name)]

    player_name_all_games = f'{player_name} Average'
    avg_rating = _calculate_avg_rating(defense_player=defense_player, offense_player=offense_player)
    nr_games = _calculate_number_of_games(defense_player=defense_player, offense_player=offense_player)

    all_games_player = Player(name=player_name_all_games, rating=avg_rating, nr_games=nr_games)

    return all_games_player


def _calculate_avg_rating(defense_player: Player, offense_player: Player) -> float:
    defense_rating = defense_player.rating
    offense_rating = offense_player.rating
    avg_rating = (offense_rating + defense_rating) / 2
    return avg_rating.round(1)


def _calculate_number_of_games(defense_player: Player, offense_player: Player) -> int:
    defense_games = defense_player.nr_games
    offense_games = offense_player.nr_games
    total_number_of_games = defense_games + offense_games
    return total_number_of_games


def _get_offense_name(player_name: str) -> str:
    return f'{player_name} Offense'


def _get_defense_name(player_name: str) -> str:
    return f'{player_name} Defense'


def _player_has_offense_and_defense_rating(player_name: str, player_lookups: dict) -> bool:
    return (_get_defense_name(player_name=player_name) in player_lookups
            and _get_offense_name(player_name=player_name) in player_lookups)


def save_ratings(ratings: list[Player]) -> None:
    filename = 'beta_ratings.csv'
    ratings.sort(reverse=True)

    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=',')

        header = ['Player', 'Position', 'Rating', '#Games']
        writer.writerow(header)

        for player in ratings:
            player_name, position = player.name.rsplit(' ', maxsplit=1)
            values = [player_name, position, player.rating, player.nr_games]
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
                      result.rating_change_players_team1]
            writer.writerow(values)


def save_readme(ratings: list[Player]) -> None:
    ratings_str = ''
    for i, player in enumerate(ratings, start=1):
        ratings_str += f'{i}. {player.name}: {player.rating} \n'

    with open('base_readme.MD', 'r') as f:
        base_readme = f.read()

    readme = base_readme.format(ratings=ratings_str)

    with open('readme.MD', 'w') as f:
        f.write(readme)


if __name__ == "__main__":
    download_game_results('results_table_football.csv')
    game_results = read_game_results('results_table_football.csv')
    ratings, calculations = get_ratings_and_calculations(game_results=game_results)
    ratings = add_avg_ratings(ratings)
    save_ratings(ratings=ratings)
    save_calculations(calculations=calculations)
    save_readme(ratings=ratings)
