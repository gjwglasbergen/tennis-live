from dataclasses import dataclass


@dataclass(frozen=True)
class MatchConfig:
    """Configuration for a tennis match."""

    sets_to_win: int = 2
    final_set_super_tiebreak: bool = False


@dataclass(frozen=True)
class Score:
    "Represents the score of a tennis match."

    sets: tuple[
        tuple[int, int], ...
    ]  # List of tuples representing the score of each set e.g ((6, 4), (3, 6), (7, 5))
    games: tuple[int, int]  # Current game score (player1, player2)
    points: tuple[int, int]  # Current point raw points (0,1)
    in_tiebreak: bool = False  # Whether the current game is a tiebreak
    winner: int | None = None  # 0 for player1, 1 for player2, None if match is ongoing


def calculate_score(points: list[int], config: MatchConfig = MatchConfig()) -> Score:
    """Calculates the score of a tennis match based on the points scored by each player.

    Args:
        points (list[int]): A list of integers representing the points scored by each player.
        config (MatchConfig): Configuration for the match."""

    raise NotImplementedError("Score calculation logic is not implemented yet.")


def display_points(score: Score) -> str:
    """Returns a string representation of the current point score.

    Args:
        score (Score): The current score of the match.

    Returns:
        str: A string representing the current point score.
    """
    raise NotImplementedError("Display points logic is not implemented yet.")
