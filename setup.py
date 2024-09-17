#!/usr/bin/env python

import os

# Always prefer setuptools over distutils
from importlib.util import module_from_spec, spec_from_file_location

from setuptools import find_namespace_packages, setup

# https://packaging.python.org/guides/single-sourcing-package-version/
# http://blog.ionelmc.ro/2014/05/25/python-packaging/

_PATH_ROOT = os.path.dirname(__file__)
_PATH_SOURCE = os.path.join(_PATH_ROOT, "src")


def _load_py_module(fname: str, pkg: str = "challenge_xyz"):  # noqa: ANN202
    spec = spec_from_file_location(os.path.join(pkg, fname), os.path.join(_PATH_SOURCE, pkg, fname))
    py = module_from_spec(spec)
    spec.loader.exec_module(py)
    return py


_about = _load_py_module("__about__.py")


def _load_requirements(path_dir: str = _PATH_ROOT, comment_char: str = "#") -> list:
    with open(os.path.join(path_dir, "requirements.txt")) as file:
        lines = [ln.strip() for ln in file.readlines()]
    reqs = [ln[: ln.index(comment_char)] if comment_char in ln else ln for ln in lines]
    return [ln for ln in reqs if ln and not any(s in ln for s in ["http://", "https://"])]


def _load_long_description(homepage: str, version: str) -> str:
    url = os.path.join(homepage, "raw", version, "docs")
    with open("README.md", encoding="utf-8") as fp:
        text = fp.read()
    # replace relative repository path to absolute link to the release
    text = text.replace("](docs", f"]({url}")
    # SVG images are not readable on PyPI, so replace them  with PNG
    return text.replace(".svg", ".png")


# https://packaging.python.org/discussions/install-requires-vs-requirements /
# keep the meta-data here for simplicity in reading this file... it's not obvious
# what happens and to non-engineers they won't know to look in init ...
# the goal of the project is simplicity for researchers, don't want to add too much
# engineer specific practices
if __name__ == "__main__":
    setup(
        name="kaggle-sandbox",
        version=_about.__version__,
        description=_about.__docs__,
        author=_about.__author__,
        author_email=_about.__author_email__,
        url=_about.__homepage__,
        license=_about.__license__,
        packages=find_namespace_packages(where="src"),
        package_dir={"": "src"},
        long_description=_load_long_description(_about.__homepage__, _about.__version__),
        long_description_content_type="text/markdown",
        include_package_data=True,
        zip_safe=False,
        keywords=["deep learning", "pytorch", "AI"],
        python_requires=">=3.6",
        setup_requires=[],
        install_requires=_load_requirements(_PATH_ROOT),
        project_urls={
            "Source Code": _about.__homepage__,
        },
        classifiers=[
            "Environment :: Console",
            "Natural Language :: English",
            # How mature is this project? Common values are
            #   3 - Alpha, 4 - Beta, 5 - Production/Stable
            "Development Status :: 3 - Alpha",
            # Indicate who your project is intended for
            "Intended Audience :: Developers",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Scientific/Engineering :: Image Recognition",
            "Topic :: Scientific/Engineering :: Information Analysis",
            # Pick your license as you wish
            # 'License :: OSI Approved :: BSD License',
            "Operating System :: OS Independent",
            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            "Programming Language :: Python :: 3",
        ],
    )
