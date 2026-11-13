# test_bug3_logic.py
from bug3_logic import find_max


def test_max_is_first():
    assert find_max([10, 5, 3]) == 10


def test_max_is_in_middle():
    assert find_max([3, 9, 2, 1]) == 9


def test_max_is_last():
    assert find_max([3, 5, 10]) == 10


def test_single_score():
    assert find_max([7]) == 7
