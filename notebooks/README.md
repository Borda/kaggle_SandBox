# Notebooks

This folder is intended for storing Jupyter notebooks related to exploration, data analysis, and experimentation for the Kaggle challenges.

Please format notebooks as percent-style Python scripts. This keeps notebooks reviewable in git while still opening as cells in tools that understand the IPython/Jupytext/VS Code percent format.

Use these cell markers:

```python
# %% [markdown]
# # Markdown heading
#
# Markdown cells are written as comment-prefixed Markdown lines.

# %%
print("Code cells use plain Python after a # %% marker.")
```

Rules:

- Use `# %% [markdown]` for prose, headings, assumptions, and experiment notes.
- Use `# %%` for executable Python code.
- Do not use a module docstring as notebook prose; it remains a Python code-cell artifact, not a markdown cell.
- Prefer top-level cell flow over a single `main()` wrapper. A notebook script should read as ordered cells: configure, load data, inspect, train, predict, validate, write outputs.
- Keep one logical step per cell: setup, data loading, validation, model, prediction, output writing.

## Convert With Jupytext

Run Jupytext with `uvx` when you need an `.ipynb` copy:

```bash
uvx --from jupytext jupytext --version
```

Convert a percent-script notebook to `.ipynb`:

```bash
uvx --from jupytext jupytext --to ipynb notebooks/00_baseline.py
```

Convert an `.ipynb` notebook back to percent-script Python:

```bash
uvx --from jupytext jupytext --to py:percent notebooks/00_baseline.ipynb
```

To keep both files paired while editing, set the notebook formats once:

```bash
uvx --from jupytext jupytext --set-formats ipynb,py:percent notebooks/00_baseline.ipynb
```

Start with `00_baseline.py`. It is intentionally simple: it copies Kaggle's `sample_submission.csv` into `outputs/baseline.csv` and validates the generated file shape with `challenge_xyz` utilities. Replace that baseline with model predictions once the data and metric are understood.

Notebook scripts are not collected by pytest because they may execute data-dependent top-level cells. Shared behavior that needs automated coverage should live in `src/challenge_xyz/` and be tested from `tests/`.
