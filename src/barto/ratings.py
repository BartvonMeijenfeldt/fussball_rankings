from collections import UserDict
from dataclasses import dataclass


class Ratings(UserDict):
    def __init__(self, init_rating=1500):
        self.init_rating = init_rating
        super().__init__()

    def __missing__(self, name):
        return Player(name, rating=self.init_rating, nr_games=0)


@dataclass
class Player:
    name: str
    rating: float
    nr_games: int

    def __add__(self, rating_gain: float):
        self.rating = round(self.rating + rating_gain, ndigits=1)
        self.nr_games += 1
        return self

    def __lt__(self, other_player):
        return self.rating < other_player.rating
