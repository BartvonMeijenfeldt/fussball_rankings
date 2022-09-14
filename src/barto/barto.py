from collections import defaultdict


class BartoRatings:
    def __init__(self, team_size: int, init_rating: float, sd_rating: float, sd_game: float) -> None:
        """Keeps track of and calculates the ratings using the Barto Method.

        Parameters
        ----------
        team_size
            The number of players in a team.
        init_rating
            The number for which new ratings will be initialized.
        sd_rating
            The (assumed) uncertainty measured in standard deviation of the rating of all the players.
        sd_day
            The (assumed) standard deviation of a player's game form.
        """
        self.team_size = team_size
        self._ratings = defaultdict(lambda: init_rating)
        self.sd_rating = sd_rating
        self.sd_game = sd_game

    def add_result(self, game_result) -> None:
        pass

    @property
    def ratings(self):
        return self._ratings.copy()

    def get_player_rating(self, player: str) -> float:
        if player not in self._ratings:
            raise ValueError(f'{player} has no rating')

        return self._ratings[player]
