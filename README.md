# Python Local `.venv` Kernel

[![Github](https://img.shields.io/badge/goerz-python--localvenv--kernel-blue.svg?logo=github)](https://github.com/goerz/python-localvenv-kernel)
[![Build Status](https://github.com/goerz/python-localvenv-kernel/workflows/CI/badge.svg)](https://github.com/goerz/python-localvenv-kernel/actions)
[![PyPI](https://img.shields.io/pypi/v/python-localvenv-kernel.svg)](https://pypi.org/project/python-localvenv-kernel/)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/python-localvenv-kernel.svg)](https://anaconda.org/conda-forge/python-localvenv-kernel)
[![Conda Recipe](https://img.shields.io/badge/recipe-conda--forge-green.svg)](https://github.com/conda-forge/python-localvenv-kernel-feedstock)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A Jupyter kernel that delegates to `ipykernel` in the `.venv` environment of a project folder.

Derived from [`poetry-kernel`](https://github.com/pathbird/poetry-kernel), see the [FAQ](https://github.com/goerz/python-localvenv-kernel/blob/master/FAQ.md#how-does-this-kernel-differ-from-poetry-kernel).


## Installation

The `python-localvenv-kernel` package can be installed via `pip` (`pip install python-localvenv-kernel`) or as a [Conda package](https://github.com/conda-forge/python-localvenv-kernel-feedstock#about-python-localvenv-kernel-feedstock) (`conda install python-localvenv-kernel`).

It must be installed into the same environment as the Jupyter server, see [Usage](#usage) below.


## Usage

* Jupyter and the `python-localvenv-kernel` package should be installed in the same environment
* The project folder must have a virtual (project) environment instantiated in a subfolder `.venv`. The name of folder can be overridden by setting the environment variable `KERNEL_VENV` (see [FAQ](https://github.com/goerz/python-localvenv-kernel/blob/master/FAQ.md#how-can-i-change-the-directory-for-the-virtual-environment))
* The project environment must include the `ipykernel` package (but not `jupyter`)
* Start Jupyter from the project folder
* Select the "Python (local .venv)" kernel

![Jupyter launcher screenshot (kernel selector)](https://github.com/goerz/python-localvenv-kernel/blob/master/.static/jupyter-screenshot.png)

![Jupyter launcher screenshot (notebook)](https://github.com/goerz/python-localvenv-kernel/blob/master/.static/jupyter-screenshot-2.png)


## FAQ

[See `FAQ.md`.][FAQ]

[FAQ]: https://github.com/goerz/python-localvenv-kernel/blob/master/FAQ.md
