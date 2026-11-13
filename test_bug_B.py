from bug3_logic import find_max


def test_single_score():
    assert find_max([7]) == 7


def test_returns_largest_score():
    assert find_max([3, 10, 5]) == 10


def test_handles_negative_scores():
    assert find_max([-8, -2, -5]) == -2


def test_handles_duplicate_maximum():
    assert find_max([4, 9, 9, 1]) == 9
