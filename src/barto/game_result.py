from dataclasses import dataclass


@dataclass(frozen=True)
class GameResult:
    Team1: list[str]
    Team2: list[str]
    PointsTeam1: int
    PointsTeam2: int

    def __post_init__(self):
        if len(self.Team1) != len(self.Team2):
            message = f'Nr of players in team 1 (n={len(self.Team1)}) is unequal to team 2 (n={len(self.Team2)})'
            raise ValueError(message)
