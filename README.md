# 🏁 Kaggle sandbox

[![CI complete testing](https://github.com/Borda/kaggle_sandbox/actions/workflows/ci_testing.yml/badge.svg?branch=main&event=push)](https://github.com/Borda/kaggle_sandbox/actions/workflows/ci_testing.yml)
[![codecov](https://codecov.io/gh/Borda/kaggle_sandbox/branch/main/graph/badge.svg)](https://codecov.io/gh/Borda/kaggle_sandbox)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Borda/kaggle_sandbox/main.svg)](https://results.pre-commit.ci/latest/github/Borda/kaggle_sandbox/main)

A small Python 3.10+ template for Kaggle competitions. It keeps a real
installable placeholder helper package in `src/challenge_xyz/` so shared
functions can be used from scripts, notebooks, and Kaggle package resources.
Forks should rename `challenge_xyz` to the competition package name once the
project stops being a template. The package is intentionally small: put shared
functions there, then import them from multiple Kaggle notebooks.

## ⚡ Quickstart

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

## 🗂️ Project Layout

```text
.
├── src/challenge_xyz/  # reusable helper package shared by scripts and notebooks
├── notebooks/          # percent-format notebook scripts with # %% cell markers
├── resources/          # lightweight notes, links, and metadata
├── tests/              # doctests and regression tests for shared helpers
├── data/               # optional local competition files, ignored by git
└── outputs/            # optional local generated files, ignored by git
```

## ⚙️ Development Checks

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

## 📋 Template Checklist

When starting a new competition, update or add:

- `COMPETITION` slug in docs, scripts, and CI examples if needed.
- Data input paths used by Kaggle notebooks.
- Validation split and metric notes.
- Shared helpers that are reused by more than one notebook.
- Output tracking notes: date, code version, notebook version, public/private score.
- Seeds at every entry point that uses randomness.
- Tests for shared helpers: empty inputs, missing files, malformed CSVs, and
  shape or dtype checks for tensor code.

## 🌟 Showcases

### Some derived projects:

- [Multiple image classification](https://github.com/Borda/kaggle_image-classify)
  - [Herbarium 2022](https://www.kaggle.com/competitions/herbarium-2022-fgvc9)
  - [Plant Pathology 2021 - FGVC8](https://www.kaggle.com/c/plant-pathology-2021-fgvc8)
  - [iMet Collection 2021 - FGVC8](https://www.kaggle.com/c/imet-2021-fgvc8)
  - [Cassava Leaf Disease Classification](https://www.kaggle.com/c/cassava-leaf-disease-classification/overview)
- [Multiple image segmentation](https://github.com/Borda/kaggle_image-segm)
  - [UW-Madison GI Tract Image Segmentation](https://www.kaggle.com/competitions/uw-madison-gi-tract-image-segmentation)
  - [Sartorius Cell Instance Segmentation](https://www.kaggle.com/c/sartorius-cell-instance-segmentation)
- [COVID detection](https://borda.github.io/kaggle_COVID-detection/)
- [Brain Tumor 3D](https://github.com/Borda/kaggle_vol-3D-classify)

### Selected Kaggle notebooks:

- [AMIA X-Ray: Inference RF-DETR detections](https://www.kaggle.com/code/jirkaborovec/amia-x-ray-inference-rf-detr-detections)
- [AMIA X-Ray: EDA baseline RF-DETR detect](https://www.kaggle.com/code/jirkaborovec/amia-x-ray-eda-baseline-rf-detr-detect)
- [Pig Posture: EDA + baseline RF-DETR detect](https://www.kaggle.com/code/jirkaborovec/pig-posture-eda-baseline-rf-detr-detect)
- [ROGII drill: geosteer + LightGBM/CatBoost/Ridge](https://www.kaggle.com/code/jirkaborovec/rogii-drill-geosteer-lightgbm-catboost-ridge)
- [Surface: train+inference 3D segmentation and GPU augment](https://www.kaggle.com/code/jirkaborovec/surface-train-inference-3d-segm-gpu-augment)
- [Surface: nnUNet training + inference with 2xT4](https://www.kaggle.com/code/jirkaborovec/surface-nnunet-training-inference-with-2xt4)
- [Surface: EDA interactive image/mask 3D view](https://www.kaggle.com/code/jirkaborovec/surface-eda-interactive-img-mask-3d-view)
- [CSIRO Img2Bio: EDA + XGBoost + DINOv3 features](https://www.kaggle.com/code/jirkaborovec/csiro-img2bio-eda-xgboost-dinov3-features)
- [Cancer Subtype: Lightning Torch inference tiles](https://www.kaggle.com/code/jirkaborovec/cancer-subtype-lightning-torch-inference-tiles)
- [Credit Risk: EDA and XGBoost depth=0+ GPU](https://www.kaggle.com/code/jirkaborovec/credit-risk-eda-xgboost-depth-0-gpu)
- [IceCube: Neutrino fitting 3D points cloud](https://www.kaggle.com/code/jirkaborovec/icecube-neutrino-fitting-3d-points-cloud)
- [BirdCLEF: Lightning Flash inference](https://www.kaggle.com/code/jirkaborovec/birdclef-lightning-flash-inference)

### Selected writing:

- [Tackling the Kaggle COVID Detection Challenge with Lightning Flash and IceVision](https://medium.com/codex/tackle-covid-detection-with-lightning-flash-and-icevision-3f66f28c24ac)
- [Easy Kaggle Offline Submission With Chaining Kernel Notebooks](https://towardsdatascience.com/easy-kaggle-offline-submission-with-chaining-kernels-30bba5ea5c4d)
- [Simple 3D MRI classification ranked bronze on Kaggle](https://towardsdatascience.com/simple-3d-mri-classification-ranked-bronze-on-kaggle-87edfdef018a/)
- [Kaggle hacking: Validate a simple hypothesis against a hidden dataset](https://towardsdatascience.com/kaggle-hacking-validate-a-simple-hypothesis-against-a-hidden-dataset-4cf02bb16510/)
- [How to organize a medical imaging challenge: Lessons from ANHIR](https://medium.com/data-science-collective/how-to-organize-a-medical-imaging-challenge-lessons-from-anhir-15fd486adbf2)
- [The Open-Source Shepherd: Why Your Best Work Is Building a Project That Doesn't Need You](https://medium.com/codex/the-open-source-shepherd-why-your-best-work-is-building-a-project-that-doesnt-need-you-bfd0641f5aca)
- [What Is Your Python Package's Public API, Really?](https://medium.com/codex/what-is-your-python-packages-public-api-really-3ff64a75bf7f)

## 🔗 References

- [Kaggle CLI](https://github.com/Kaggle/kaggle-api)
- [KaggleHub](https://github.com/Kaggle/kagglehub)
- [Python Packaging User Guide](https://packaging.python.org/)
- [Jirka Borovec on Kaggle](https://www.kaggle.com/jirkaborovec)
- [Jirka Borovec public Kaggle notebooks](https://www.kaggle.com/jirkaborovec/code)
- [Jirka Borovec on Medium](https://medium.com/@jborovec)
