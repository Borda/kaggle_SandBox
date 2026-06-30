"""Shared utility functions for Kaggle notebooks."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class CsvShape:
    """Describe a CSV file by header and row count.

    This small value object is useful in Kaggle notebooks where several cells
    need to compare generated outputs against reference files.

    Args:
        path: CSV file path.
        columns: CSV header columns, in order.
        row_count: Number of data rows excluding the header.

    Returns:
        None.

    Raises:
        None.

    Example:
        >>> CsvShape(Path("sample.csv"), ("id", "target"), 2).row_count
        2
    """

    path: Path
    columns: tuple[str, ...]
    row_count: int


def read_csv_shape(path: str | Path) -> CsvShape:
    """Read a CSV file header and row count.

    Args:
        path: CSV file path.

    Returns:
        CSV shape with columns and data-row count.

    Raises:
        FileNotFoundError: If `path` does not exist.
        ValueError: If the CSV file is empty.

    Example:
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as tmp:
        ...     csv_path = Path(tmp) / "data.csv"
        ...     newline = chr(10)
        ...     _ = csv_path.write_text(f"id,target{newline}1,0{newline}", encoding="utf-8")
        ...     read_csv_shape(csv_path).columns
        ('id', 'target')
    """
    csv_path = Path(path)
    with csv_path.open(newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        try:
            header = tuple(next(reader))
        except StopIteration as ex:
            msg = f"CSV file is empty: {csv_path}"
            raise ValueError(msg) from ex
        return CsvShape(path=csv_path, columns=header, row_count=sum(1 for _ in reader))


def assert_same_csv_shape(reference: str | Path, candidate: str | Path) -> CsvShape:
    """Assert that two CSV files have the same header and row count.

    Args:
        reference: Reference CSV path.
        candidate: Candidate CSV path.

    Returns:
        Shape of the candidate CSV.

    Raises:
        FileNotFoundError: If either CSV file does not exist.
        ValueError: If columns or row count differ.

    Example:
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as tmp:
        ...     reference = Path(tmp) / "reference.csv"
        ...     candidate = Path(tmp) / "candidate.csv"
        ...     newline = chr(10)
        ...     _ = reference.write_text(f"id,target{newline}1,0{newline}", encoding="utf-8")
        ...     _ = candidate.write_text(f"id,target{newline}1,1{newline}", encoding="utf-8")
        ...     assert_same_csv_shape(reference, candidate).row_count
        1
    """
    reference_shape = read_csv_shape(reference)
    candidate_shape = read_csv_shape(candidate)

    if reference_shape.columns != candidate_shape.columns:
        msg = f"CSV columns do not match: expected {reference_shape.columns}, got {candidate_shape.columns}"
        raise ValueError(msg)
    if reference_shape.row_count != candidate_shape.row_count:
        msg = f"CSV row count does not match: expected {reference_shape.row_count}, got {candidate_shape.row_count}"
        raise ValueError(msg)

    return candidate_shape
