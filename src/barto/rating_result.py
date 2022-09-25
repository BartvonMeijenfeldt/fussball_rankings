from dataclasses import dataclass, field


@dataclass
class RatingResult:
    team1: list[str]
    team2: list[str]
    points_team1: int
    points_team2: int
    rating_advantage: float
    expected_percent_score: float
    achieved_percent_score: float = field(init=False)
    rating_gain_players_team1: float

    def __post_init__(self):
        self.achieved_percent_score = self.points_team1 / (self.points_team1 + self.points_team2)
