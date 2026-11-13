import pytest
from load_scores import load_scores

def test_scores_file():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5
    assert len(skipped) == 5

def test_blank_line(tmp_path):
    path = tmp_path / "blank.csv"
    path.write_text("name,score\n\n학생,80\n", encoding="utf-8")
    assert load_scores(path) == ([("학생", 80)], [])

def test_quoted_name(tmp_path):
    path = tmp_path / "quoted.csv"
    path.write_text('name,score\n"김,하나",80\n', encoding="utf-8")
    assert load_scores(path) == ([("김,하나", 80)], [])

def test_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_scores(tmp_path / "missing.csv")

def test_header_only():
    kept, skipped = load_scores("empty.csv")
    assert kept == []
    assert skipped == []

@pytest.mark.parametrize("score, valid", [
    (-1, False), (0, True), (1, True),
    (99, True), (100, True), (101, False),
])
def test_boundary(tmp_path, score, valid):
    path = tmp_path / "case.csv"
    path.write_text(f"name,score\n학생,{score}\n", encoding="utf-8")
    kept, skipped = load_scores(path)
    assert kept == ([("학생", score)] if valid else [])
    assert len(skipped) == (0 if valid else 1)

def test_weird_file():
    kept, skipped = load_scores("weird.csv")
    assert kept == [("한겨울", 77), ("윤보람", 88)]
    assert len(skipped) == 7
    assert skipped[0][0] == 2
    assert skipped[0][2] == "이름이 비어 있음"
