from dataclasses import dataclass


@dataclass(frozen=True)
class GameResult:
    team1: list[str]
    team2: list[str]
    points_team1: int
    points_team2: int

    def __post_init__(self):
        self._assert_teams_same_length()
        self._assert_points_team_nonnegative()

    def _assert_teams_same_length(self):
        if len(self.team1) != len(self.team2):
            message = f'Nr of players in team 1 (n={len(self.team1)}) is unequal to team 2 (n={len(self.team2)})'
            raise AttributeError(message)

    def _assert_points_team_nonnegative(self):
        if self.points_team1 < 0:
            message = f'Nr of points team 1 is negative. Points team 1: {self.points_team1})'
            raise AttributeError(message)

        if self.points_team2 < 0:
            message = f'Nr of points team 2 is negative. Points team 2: {self.points_team2})'
            raise AttributeError(message)

    @property
    def nr_points_played(self) -> int:
        return self.points_team1 + self.points_team2

    @property
    def team_size(self) -> int:
        return len(self.team1)
