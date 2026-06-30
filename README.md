# Kaggle sandbox

[![CI complete testing](https://github.com/Borda/kaggle_sandbox/actions/workflows/ci_testing.yml/badge.svg?branch=main&event=push)](https://github.com/Borda/kaggle_sandbox/actions/workflows/ci_testing.yml)
[![codecov](https://codecov.io/gh/Borda/kaggle_sandbox/branch/main/graph/badge.svg)](https://codecov.io/gh/Borda/kaggle_sandbox)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Borda/kaggle_sandbox/main.svg)](https://results.pre-commit.ci/latest/github/Borda/kaggle_sandbox/main)

A small Python 3.10+ template for Kaggle competitions. It keeps a real
installable placeholder helper package in `src/challenge_xyz/` so shared
functions can be used from scripts, notebooks, and Kaggle package resources.
Forks should rename `challenge_xyz` to the competition package name once the
project stops being a template. The package is intentionally small: put shared
functions there, then import them from multiple Kaggle notebooks.

## Quickstart

Create an environment and install the template:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade uv
uv sync --group dev --extra kaggle
```

On Kaggle, attach this repository or a built wheel as a resource, then install
the helper package from that attached path:

```bash
pip install /kaggle/input/<resource-name>
```

Then import shared helpers from notebook cells:

```python
from challenge_xyz import assert_same_csv_shape, read_csv_shape
```

For local smoke checks, install the package editable and run tests:

```bash
uv sync --group dev
uv run --group dev pytest -q
```

## Project Layout

- `src/challenge_xyz/`: reusable placeholder helper package shared by scripts and notebooks.
- `notebooks/`: notebook-compatible Python scripts with `# %%` cell markers.
- `resources/`: links, notes, and lightweight metadata; not raw datasets/models.
- `data/`: optional local competition files, ignored by git.
- `outputs/`: optional local generated files, ignored by git.
- `tests/`: doctests and regression tests for template helpers.

## Development Checks

```bash
uv run --group dev ruff check .
uv run --group dev pytest -q
uv build
uv run --group dev twine check dist/*
```

For a full local pre-commit pass:

```bash
uv run --group dev pre-commit run --all-files
```

## Template Checklist

When starting a new competition, update or add:

- `COMPETITION` slug in docs, scripts, and CI examples if needed.
- Data input paths used by Kaggle notebooks.
- Validation split and metric notes.
- Shared helpers that are reused by more than one notebook.
- Output tracking notes: date, code version, notebook version, public/private score.
- Seeds at every entry point that uses randomness.
- Tests for shared helpers: empty inputs, missing files, malformed CSVs, and
  shape or dtype checks for tensor code.

## References

- [Kaggle CLI](https://github.com/Kaggle/kaggle-api)
- [KaggleHub](https://github.com/Kaggle/kagglehub)
- [Python Packaging User Guide](https://packaging.python.org/)
- [Jirka Borovec on Kaggle](https://www.kaggle.com/jirkaborovec)
- [Jirka Borovec public Kaggle notebooks](https://www.kaggle.com/jirkaborovec/code)
- [Jirka Borovec on Medium](https://medium.com/@jborovec)
