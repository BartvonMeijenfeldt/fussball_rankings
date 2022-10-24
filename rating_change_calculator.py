import argparse

from src.barto.barto import BartoCalculator


parser = argparse.ArgumentParser()
parser.add_argument("--prior_rating_advantage", type=int, help="Rating advantage from perspective team 1")
parser.add_argument("--points_team1", type=int, help="Points scored by team 1")
parser.add_argument("--points_team2", type=int, help="Points scored by team 2")
args = parser.parse_args()


calculator = BartoCalculator(sd_rating=100, sd_game_performance=100, rating_scale=1 / 400)
calculator.get_rating_gain()

