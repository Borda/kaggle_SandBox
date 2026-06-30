# %% [markdown]
# # Baseline Kaggle Submission
#
# Run this script after downloading and unzipping competition files into
# `data/`. The baseline copies Kaggle's `sample_submission.csv` into
# `outputs/baseline.csv` and validates the generated file shape.

# %%
from __future__ import annotations

import os
import shutil
from pathlib import Path

from challenge_xyz import assert_same_csv_shape

# %% [markdown]
# ## Configuration
#
# Keep reusable helpers in `challenge_xyz`; keep notebook-specific paths and
# experiment choices in notebook cells.

# %%
data_dir = Path(os.environ.get("KAGGLE_DATA_DIR", "data"))
output_dir = Path(os.environ.get("KAGGLE_OUTPUT_DIR", "outputs"))
sample_file = data_dir / "sample_submission.csv"
baseline_file = output_dir / "baseline.csv"

# %% [markdown]
# ## Create Baseline Submission
#
# This intentionally copies the sample file. It is not a useful model; it is a
# notebook smoke test before real predictions are added.

# %%
output_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(sample_file, baseline_file)

# %% [markdown]
# ## Validate Submission Shape
#
# The generated CSV should have the same columns and row count as the reference.

# %%
shape = assert_same_csv_shape(sample_file, baseline_file)
print(f"Wrote {shape.path} with {shape.row_count} rows.")
