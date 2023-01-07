# Script to calculate rating changes
import argparse

from barto.barto import BartoCalculator


parser = argparse.ArgumentParser()
parser.add_argument("--prior_rating_advantage", type=float, help="Prior rating advantage from perspective team 1")
parser.add_argument("--points_team1", type=int, help="Points scored by team 1")
parser.add_argument("--points_team2", type=int, help="Points scored by team 2")
args = parser.parse_args()


calculator = BartoCalculator(sd_rating=100, sd_game_performance=100, rating_scale=1 / 400)
rating_gain = calculator.get_rating_change(prior_rating_advantage=args.prior_rating_advantage,
                                           n_contests=args.points_team1 + args.points_team2,
                                           constests_won=args.points_team1)
player_gain = round(rating_gain / 2, 1)
print(player_gain)
