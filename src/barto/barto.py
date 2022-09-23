from dataclasses import dataclass
import math

from collections import defaultdict
from scipy import integrate, stats, optimize

from src.barto.game_result import GameResult


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
        self._ratings = defaultdict(lambda: init_rating)
        self._calculator = BartoCalculator(sd_rating=sd_rating,
                                           sd_game_performance=sd_game_performance,
                                           rating_scale=self.rating_scale)

    def add_results(self, results: list[GameResult]) -> None:
        for game_result in results:
            self.add_single_result(game_result=game_result)

    def add_single_result(self, game_result: GameResult) -> None:
        rating_gain_team1 = self._get_rating_gain(game_result=game_result)
        self._update_ratings(game_result, rating_gain_team1)

    def _get_rating_difference(self, game_result: GameResult) -> float:
        rating_team1 = self.get_team_rating(game_result.team1)
        rating_team2 = self.get_team_rating(game_result.team2)
        return rating_team1 - rating_team2

    def _get_rating_gain(self, game_result: GameResult) -> float:
        rating_advantage_team1 = self._get_rating_difference(game_result)

        rating_gain_team1 = self._calculator.get_rating_gain(
            prior_rating_advantage=rating_advantage_team1,
            n_contests=game_result.nr_points_played,
            constests_won=game_result.points_team1)

        return rating_gain_team1

    def _update_ratings(self, game_result: GameResult, rating_gain_team1: float) -> None:
        self._update_ratings_team(team=game_result.team1, rating_gain_team=rating_gain_team1)
        self._update_ratings_team(team=game_result.team2, rating_gain_team=-1 * rating_gain_team1)

    def _update_ratings_team(self, team: list[str], rating_gain_team: float) -> None:
        player_rating_gain = rating_gain_team / len(team)

        for player in team:
            new_player_rating = self._ratings[player] + player_rating_gain
            rounded_new_player_rating = round(new_player_rating, ndigits=1)
            self._ratings[player] = rounded_new_player_rating

    @property
    def ratings(self):
        return self._ratings.copy()

    def get_team_rating(self, team: list[str]) -> float:
        player_ratings = [self.get_player_rating(player) for player in team]
        team_rating = sum(player_ratings)
        return team_rating

    def get_player_rating(self, player: str) -> float:
        return self._ratings[player]


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
    max_rating_gain
        The max team rating gain that can be obtained in a single game
    max_performance_diff
        The max difference between the team performance difference with respect to the teams (posterior) rating
        difference.
    """
    sd_rating: float
    sd_game_performance: float
    rating_scale: float = 1 / 400
    max_rating_gain: float = 100
    max_performance_diff: float = 300

    def get_rating_gain(self, prior_rating_advantage: float, n_contests: float, constests_won: float):
        """Get rating gain team 1.

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
            Rating gain team 1.
        """
        self._set_game_results(prior_rating_advantage, n_contests, constests_won)
        neg_unnormalized_posterior = self._get_neg_unnormalized_posterior()
        rating_gain_team1 = self._optimize_posterior(neg_unnormalized_posterior)

        return rating_gain_team1

    def _set_game_results(self, prior_rating_advantage: float, n_contests: float, constests_won: float) -> None:
        self.prior_rating_advantage = prior_rating_advantage
        self.n_contests = n_contests
        self.contests_won = constests_won

    def _get_neg_unnormalized_posterior(self) -> callable:
        def neg_unnormalized_posterior(rating_gain: float) -> float:
            likelhood_bayes = self._get_likelihood_bayes()
            prior_bayes = self._get_prior_bayes()
            unnormalized_posterior = likelhood_bayes(rating_gain) * prior_bayes(rating_gain)
            neg_unnormalized_posterior = -1 * unnormalized_posterior
            return neg_unnormalized_posterior

        return neg_unnormalized_posterior

    def _get_likelihood_bayes(self) -> callable:
        def likelihood(rating_gain: float) -> float:
            def f(performance_diff: float) -> float:
                performance_diff_probability = self._get_performance_diff_probability_density(
                    performance_diff=performance_diff, rating_gain=rating_gain)
                game_outcome_probability = self._get_game_outcome_probability_mass(performance_diff=performance_diff)
                return performance_diff_probability * game_outcome_probability

            value, _ = integrate.quad(f, a=-1 * self.max_performance_diff, b=self.max_performance_diff)
            return value

        return likelihood

    def _get_performance_diff_probability_density(self, performance_diff: float, rating_gain: float) -> float:
        posterior_rating_diff = self.prior_rating_advantage + 2 * rating_gain
        return stats.norm.pdf(x=performance_diff, loc=posterior_rating_diff, scale=self.sd_game_performance)

    def _get_game_outcome_probability_mass(self, performance_diff: float) -> float:
        probability_winning_contest = self._get_probability_winning_contest(performance_diff=performance_diff)
        return stats.binom.pmf(k=self.contests_won, n=self.n_contests, p=probability_winning_contest)

    def _get_probability_winning_contest(self, performance_diff: float) -> float:
        return 1 / (1 + math.exp(-1 * performance_diff * self.rating_scale))

    def _get_prior_bayes(self) -> callable:
        def prior(rating_gain: float) -> float:
            return stats.norm.pdf(x=rating_gain, loc=0, scale=self.sd_rating)
        return prior

    def _optimize_posterior(self, neg_unnormalized_posterior: callable) -> float:
        rating_gain_bounds = [-self.max_rating_gain, self.max_rating_gain]
        result = optimize.minimize_scalar(neg_unnormalized_posterior, bounds=rating_gain_bounds, method='brent')
        rating_gain = result.x
        return rating_gain
