from pathlib import Path

import pytest

from challenge_xyz import assert_same_csv_shape, read_csv_shape


def _write_csv(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def test_read_csv_shape_returns_columns_and_row_count(tmp_path: Path) -> None:
    csv_path = tmp_path / "data.csv"
    _write_csv(csv_path, "id,target\n1,0\n2,1\n")

    shape = read_csv_shape(csv_path)

    assert shape.columns == ("id", "target")
    assert shape.row_count == 2


def test_assert_same_csv_shape_accepts_matching_schema(tmp_path: Path) -> None:
    reference = tmp_path / "reference.csv"
    candidate = tmp_path / "candidate.csv"
    _write_csv(reference, "id,target\n1,0\n2,0\n")
    _write_csv(candidate, "id,target\n1,1\n2,0\n")

    result = assert_same_csv_shape(reference, candidate)

    assert result.columns == ("id", "target")
    assert result.row_count == 2


def test_assert_same_csv_shape_rejects_header_mismatch(tmp_path: Path) -> None:
    reference = tmp_path / "reference.csv"
    candidate = tmp_path / "candidate.csv"
    _write_csv(reference, "id,target\n1,0\n")
    _write_csv(candidate, "row_id,target\n1,0\n")

    with pytest.raises(ValueError, match="columns do not match"):
        assert_same_csv_shape(reference, candidate)


def test_assert_same_csv_shape_rejects_row_count_mismatch(tmp_path: Path) -> None:
    reference = tmp_path / "reference.csv"
    candidate = tmp_path / "candidate.csv"
    _write_csv(reference, "id,target\n1,0\n2,0\n")
    _write_csv(candidate, "id,target\n1,0\n")

    with pytest.raises(ValueError, match="row count does not match"):
        assert_same_csv_shape(reference, candidate)
