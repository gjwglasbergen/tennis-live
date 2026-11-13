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


def test_first_point_player2():
    raw_points = [1]
    s = calculate_score(raw_points)
    assert s.sets == ()
    assert s.games == (0, 0)
    assert s.points == (0, 1)
    assert not s.in_tiebreak
    assert s.winner is None

    assert display_points(s) == ("0", "15")


def test_win_game():
    raw_points = game(0)
    s = calculate_score(raw_points)
    assert s.sets == ()
    assert s.games == (1, 0)
    assert s.points == (0, 0)
    assert not s.in_tiebreak
    assert s.winner is None


def test_win_set():
    raw_points = set(0)
    s = calculate_score(raw_points)
    assert s.sets == ((6, 0),)
    assert s.games == (0, 0)
    assert s.points == (0, 0)
    assert not s.in_tiebreak
    assert s.winner is None


def test_6_5_set():
    raw_points = game(0) * 5 + game(1) * 5 + game(0)

    s = calculate_score(raw_points)

    assert s.sets == ()
    assert s.games == (6, 5)
    assert s.points == (0, 0)
    assert not s.in_tiebreak
    assert s.winner is None

    raw_points.extend(game(0))  # Player 1 wins the next game, set should be over
    s = calculate_score(raw_points)
    assert s.sets == ((7, 5),)
    assert s.games == (0, 0)
    assert s.points == (0, 0)
    assert not s.in_tiebreak
    assert s.winner is None


def test_deuce_and_adv():
    raw_points = [0, 1, 0, 1, 0, 1]  # 40-40
    s = calculate_score(raw_points)
    assert s.points == (3, 3)
    assert display_points(s) == ("Deuce", "Deuce")

    raw_points.append(0)  # Player 1 advantage
    s = calculate_score(raw_points)
    assert s.points == (4, 3)
    assert display_points(s) == ("Advantage", "40")

    raw_points.append(1)  # Back to deuce
    s = calculate_score(raw_points)
    assert s.points == (4, 4)

    raw_points.append(1)  # Player 2 advantage
    s = calculate_score(raw_points)
    assert s.points == (4, 5)
    assert display_points(s) == ("40", "Advantage")

    raw_points.append(1)  # Player 2 wins game
    s = calculate_score(raw_points)
    assert s.games == (0, 1)
    assert s.points == (0, 0)


def test_tiebreak():
    raw_points = game(0) * 5 + game(1) * 6 + game(0)
    s = calculate_score(raw_points)
    assert s.sets == ()
    assert s.games == (6, 6)
    assert s.points == (0, 0)
    assert s.in_tiebreak
