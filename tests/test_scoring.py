from tennis_live.scoring import calculate_score, display_points


def game(player: int) -> list[int]:
    """Helper function to simulate a game where player p wins all points."""
    return [player] * 4


def set(player: int) -> list[int]:
    """Helper function to simulate a set where player p wins all games."""
    return game(player) * 6


def test_starting_score():
    raw_points = []
    s = calculate_score(raw_points)
    assert s.sets == ()
    assert s.games == (0, 0)
    assert s.points == (0, 0)
    assert not s.in_tiebreak
    assert s.winner is None


def test_first_point_player1():
    raw_points = [0]
    s = calculate_score(raw_points)
    assert s.sets == ()
    assert s.games == (0, 0)
    assert s.points == (1, 0)
    assert not s.in_tiebreak
    assert s.winner is None

    assert display_points(s) == ("15", "0")
