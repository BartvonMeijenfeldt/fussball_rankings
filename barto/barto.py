from dataclasses import dataclass
import math
import numpy as np

from scipy import stats, optimize

from .ratings import Player, Ratings
from .game_result import GameResult
from .game_calculation import GameCalculation


class BartoRatings:
    rating_scale = 1 / 400

    def __init__(self, init_rating: float, sd_rating: float, sd_game_performance: float) -> None:
        """Keeps track of and calculates the ratings using the Barto Method.

        Parameters
        ----------
        init_rating
            The number for which new ratings will be initialized.
        sd_rating
            The (assumed) uncertainty measured in standard deviation of the rating of all the players.
        sd_day
            The (assumed) standard deviation of a player's game form.
        """
        self._ratings = Ratings(init_rating=init_rating)
        self._calculations = []
        self._calculator = BartoCalculator(sd_rating=sd_rating,
                                           sd_game_performance=sd_game_performance,
                                           rating_scale=self.rating_scale)

    def add_results(self, results: list[GameResult]) -> None:
        for game_result in results:
            self.add_single_result(game_result=game_result)

    def add_single_result(self, game_result: GameResult) -> None:
        rating_change_players_team1 = self._get_rating_change_players_team1(game_result=game_result)
        self._add_rating_result(game_result, rating_change_players_team1=rating_change_players_team1)
        self._update_ratings(game_result=game_result, rating_change_players_team1=rating_change_players_team1)

    def _get_rating_change_players_team1(self, game_result: GameResult) -> float:
        rating_advantage_team1 = self._get_rating_difference(game_result)

        rating_change_team1 = self._calculator.get_rating_change(
            prior_rating_advantage=rating_advantage_team1,
            n_contests=game_result.nr_points_played,
            constests_won=game_result.points_team1)

        rating_change_players_team1 = self._get_players_rating_change(
            rating_change_team=rating_change_team1, team_size=len(game_result.team1))

        return rating_change_players_team1

    def _get_rating_difference(self, game_result: GameResult) -> float:
        rating_team1 = self.get_team_rating(game_result.team1)
        rating_team2 = self.get_team_rating(game_result.team2)
        return rating_team1 - rating_team2

    def _update_ratings(self, game_result: GameResult, rating_change_players_team1: float) -> None:
        self._update_ratings_team(team=game_result.team1, rating_change_player=rating_change_players_team1)
        self._update_ratings_team(team=game_result.team2, rating_change_player=-1 * rating_change_players_team1)

    def _update_ratings_team(self, team: list[str], rating_change_player: float) -> None:
        for player in team:
            self._ratings[player] += rating_change_player

    @staticmethod
    def _get_players_rating_change(rating_change_team: float, team_size: int) -> float:
        return round(rating_change_team / team_size, ndigits=1)

    def _add_rating_result(self, game_result: GameResult, rating_change_players_team1: float) -> None:
        rating_advantage_team1 = self._get_rating_difference(game_result)
        expected_percent_score_team1 = self._calculator.get_expected_percent_score(
            prior_rating_advantage=rating_advantage_team1)

        rating_result = GameCalculation(
            team1=game_result.team1,
            team2=game_result.team2,
            points_team1=game_result.points_team1,
            points_team2=game_result.points_team2,
            rating_advantage=rating_advantage_team1,
            expected_percent_score=expected_percent_score_team1,
            rating_change_players_team1=rating_change_players_team1)

        self._calculations.append(rating_result)

    @property
    def ratings(self) -> list[Player]:
        return list(self._ratings.values())

    @property
    def calculations(self) -> list[GameCalculation]:
        return self._calculations.copy()

    def get_team_rating(self, team: list[str]) -> float:
        player_ratings = [self.get_player_rating(player) for player in team]
        team_rating = sum(player_ratings)
        return team_rating

    def get_player_rating(self, player: str) -> float:
        player: Player = self._ratings[player]
        return player.rating


@dataclass
class BartoCalculator:
    """Class for performing the calculations necessary for Barto ratings.

    Parameters
    ----------
    sd_rating
        Uncertainty of the estimated ratings. The quantity is expressed in standard deviation of the difference of the
        team ratings.
    sd_game_performance
        Standard deviation of the performance in a game of the team. This accounts for fluctuating performance of a
        team in games (some days people play better other days worse). The quantity is expressed in standard deviation
        of the difference of the team performance ratings.
    rating_scale
        Parameter that scales the difference in rating to an expected probability of winning a contest
    max_rating_change
        The max team rating change that can be obtained in a single game
    max_performance_diff
        The max difference between the team performance difference with respect to the teams (posterior) rating
        difference.
    """
    sd_rating: float
    sd_game_performance: float
    rating_scale: float = 1 / 400
    max_rating_change: float = 100
    max_performance_diff: float = 3000
    integration_nr_evals: int = 3000

    def get_rating_change(self, prior_rating_advantage: float, n_contests: float, constests_won: float):
        """Get rating change team 1.

        Calculated by maximum likelihood method.

        Parameters
        ----------
        prior_rating_advantage
            Rating advantages team 1 over team 2.
        n_contests
            Number of contests played.
        constests_won
            Number of contests won by team 1

        Returns
        -------
            Rating change team 1.
        """
        self._set_game_results(prior_rating_advantage, n_contests, constests_won)
        neg_unnormalized_posterior = self._get_neg_unnormalized_posterior()
        rating_change_team1 = self._optimize_posterior(neg_unnormalized_posterior)

        return rating_change_team1

    def _set_game_results(self, prior_rating_advantage: float, n_contests: float, constests_won: float) -> None:
        self.rating_diff = prior_rating_advantage
        self.n_contests = n_contests
        self.contests_won = constests_won

    def _get_neg_unnormalized_posterior(self) -> callable:
        def neg_unnormalized_posterior(rating_change: float) -> float:
            likelhood_bayes = self._get_likelihood_bayes()
            prior_bayes = self._get_prior_bayes()
            unnormalized_posterior = likelhood_bayes(rating_change) * prior_bayes(rating_change)
            neg_unnormalized_posterior = -1 * unnormalized_posterior
            return neg_unnormalized_posterior

        return neg_unnormalized_posterior

    def _get_likelihood_bayes(self) -> callable:
        def likelihood(rating_change: float) -> float:
            def f(performance_diffs: np.array) -> float:
                performance_diff_probability = self._get_performance_diff_probability_density(
                    performance_diffs=performance_diffs, rating_change=rating_change)
                game_outcome_probability = self._get_game_outcome_probability_mass(performance_diffs=performance_diffs)
                return performance_diff_probability * game_outcome_probability

            lower_bound = self.rating_diff - self.max_performance_diff
            upper_bound = self.rating_diff + self.max_performance_diff
            x = np.linspace(start=lower_bound, stop=upper_bound, num=self.integration_nr_evals)
            y = f(x)

            value = np.trapz(y=y, x=x)
            return value

        return likelihood

    def _get_performance_diff_probability_density(self, performance_diffs: np.array, rating_change: float) -> np.array:
        posterior_rating_diff = self.rating_diff + 2 * rating_change
        return stats.norm.pdf(x=performance_diffs, loc=posterior_rating_diff, scale=self.sd_game_performance)

    def _get_game_outcome_probability_mass(self, performance_diffs: np.array) -> np.array:
        probability_winning_contest = self._get_probability_winning_contest(performance_diffs=performance_diffs)
        return stats.binom.pmf(k=self.contests_won, n=self.n_contests, p=probability_winning_contest)

    def _get_probability_winning_contest(self, performance_diffs: np.array) -> np.array:
        return 1 / (1 + np.exp(-1 * performance_diffs * self.rating_scale))

    def _get_prior_bayes(self) -> callable:
        def prior(rating_change: float) -> float:
            return stats.norm.pdf(x=rating_change, loc=0, scale=self.sd_rating)
        return prior

    def _optimize_posterior(self, neg_unnormalized_posterior: callable) -> float:
        rating_change_bounds = [-self.max_rating_change, self.max_rating_change]
        result = optimize.minimize_scalar(neg_unnormalized_posterior, bounds=rating_change_bounds, method='brent')
        rating_change = result.x
        return rating_change

    def get_expected_percent_score(self, prior_rating_advantage) -> float:
        self._set_game_results(prior_rating_advantage=prior_rating_advantage, n_contests=1, constests_won=1)
        expected_percent_score = self._get_likelihood_bayes()(rating_change=0)
        return expected_percent_score
