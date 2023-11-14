# Python Local-Venv Kernel

A Jupyter kernel that delegates to the `.venv` folder in the notebook directory.

Derived from [`poetry-kernel`](https://github.com/pathbird/poetry-kernel), see the [FAQ](https://github.com/goerz/python-localvenv-kernel/blob/master/FAQ.md)

## Installation

The `python-local-venv` package must be installed into the environment as Jupyter itself.

```
pip install python-local-venv
```

```
conda install python-local-venv
```

## Usage

* Jupyter and the `python-local-venv` package should be installed in the same environment
* The project folder must have a virtual (project) environment instantiated in a subfolder `.venv`
* The project environment must include the `ipykernel` package (but not `jupyter`)
* Start Jupyter from the project folder
* Select the "Python (local .venv)"

## FAQ

[See FAQ.md.](https://github.com/goerz/python-localvenv-kernel/blob/master/FAQ.md)
