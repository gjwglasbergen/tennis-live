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
    games: tuple[int, int]  # Current game score (player0, player1)
    points: tuple[int, int]  # Current point raw points (0,1)
    in_tiebreak: bool = False  # Whether the current game is a tiebreak
    winner: int | None = None  # 0 for player0, 1 for player1, None if match is ongoing


def update_points(points_in_game: list[int], point_winner: int) -> None:
    """Updates the points in the current game based on the point winner.

    Args:
        points_in_game (list[int]): Current points in the game for both players.
        point_winner (int): The player who won the point (0 or 1).
    """
    if point_winner not in (0, 1):
        raise ValueError(f"Invalid point winner: {point_winner}. Must be 0 or 1.")

    points_in_game[point_winner] += 1


def update_games(games_in_set: list[int], game_winner: int) -> None:
    """Updates the games in the current set based on the game winner.

    Args:
        games_in_set (list[int]): Current games in the set for both players.
        game_winner (int): The player who won the game (0 or 1).
    """
    if game_winner not in (0, 1):
        raise ValueError(f"Invalid game winner: {game_winner}. Must be 0 or 1.")

    games_in_set[game_winner] += 1


def calculate_score(points: list[int], config: MatchConfig = MatchConfig()) -> Score:
    """Calculates the score of a tennis match based on the points scored by each player.

    Args:
        points (list[int]): A list of integers representing the points scored by both players.
        config (MatchConfig): Configuration for the match."""

    points_in_game = [0, 0]  # Points in the current game for player 0 and player 1
    games_in_set = [0, 0]  # Games won in the current set for player 0 and player 1
    for point in points:
        if point not in (0, 1):
            raise ValueError(f"Invalid point value: {point}. Must be 0 or 1.")

        update_points(points_in_game, point)
        if points_in_game[0] >= 4 and points_in_game[0] - points_in_game[1] >= 2:
            update_games(games_in_set, 0)
            points_in_game = [0, 0]  # Reset points for the next game
        elif points_in_game[1] >= 4 and points_in_game[1] - points_in_game[0] >= 2:
            update_games(games_in_set, 1)
            points_in_game = [0, 0]  # Reset points for the next game

    return Score(
        sets=(),
        games=tuple(games_in_set),
        points=tuple(points_in_game),
        in_tiebreak=False,
        winner=None,
    )


def display_points(score: Score) -> str:
    """Returns a string representation of the current point score.

    Args:
        score (Score): The current score of the match.

    Returns:
        str: A string representing the current point score.
    """
    raise NotImplementedError("Display points logic is not implemented yet.")
