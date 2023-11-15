# Contributing

Development of this package is driven via `make`. If you do not have `make` installed, see the [Makefile][] for the equivalent Python commands.

Run `make help` (or just `make`) to see a list of targets.


## Development installation

Run `PYTHON=<path to Python> make develop` to dev-install the package into the environment for the given `python` executable. Note that that Python environment should have Jupyter installed.

The `make develop` command is mostly equivalent to `$PYTHON -m pip install -e .`, except that an editable install will not copy the kernel file into the environment. When not using the `Makefile`, you must manually copy the `build/kernels/python-localvenv` folder to `{sys.prefix}/share/jupyter/kernels/python-localvenv`.


## Running tests locally

Run `make test`. See the [Makefile][] and [`test/test_kernel.py`](test/test_kernel.py) for details.


## Code style

Code should be formatted with `black -l 79` using the [Black formatter](https://black.readthedocs.io/en/stable/).

Apply the formatting with `make codestyle`.


## Making a release

Releases happen by simply tagging a commit as, e.g., `v1.0.0`. The version number in [`setup.py`](setup.py) must correspond to the tagged version. In between releases, the version number should have a `+dev` or `-dev` suffix, see [Inter-Release Versioning Recommendations](https://michaelgoerz.net/notes/inter-release-versioning-recommendations.html).

There is a Github workflow that will automatically upload the release to [PyPI](https://pypi.org/project/python-localvenv-kernel/).

[There also is a bot](https://conda-forge.org/docs/maintainer/updating_pkgs.html) that monitors PyPI and automatically updates the [Conda feedstock](https://github.com/conda-forge/python-localvenv-kernel-feedstock). It may take a day or so before the new release is detected, so please be patient.


[Makefile]: Makefile
