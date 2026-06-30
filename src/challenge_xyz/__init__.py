"""Kaggle competition template helpers."""

from challenge_xyz.__about__ import __author__, __author_email__, __docs__, __homepage__, __license__, __version__
from challenge_xyz.utils import CsvShape, assert_same_csv_shape, read_csv_shape

__all__ = [
    "CsvShape",
    "__author__",
    "__author_email__",
    "__docs__",
    "__homepage__",
    "__license__",
    "__version__",
    "assert_same_csv_shape",
    "read_csv_shape",
]
