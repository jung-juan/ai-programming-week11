import pandas as pd

from analysis import 정제, 반별평균


scores = pd.read_csv("scores_2026.csv")
mini = pd.read_csv("mini.csv")

정제된_scores = 정제(scores)
정제된_mini = 정제(mini)


def test_scores_2026_has_100_clean_rows():
    assert len(정제된_scores) == 100


def test_cleaned_scores_have_only_two_classes():
    assert set(정제된_scores["반"].unique()) == {"1반", "2반"}


def test_class_score_sums_equal_total_score_sum():
    반별_점수합 = 정제된_scores.groupby("반")["점수"].sum()
    assert 반별_점수합.sum() == 정제된_scores["점수"].sum()


def test_mini_first_class_average_is_80():
    평균 = 반별평균(정제된_mini)
    assert 평균["1반"] == 80.0
