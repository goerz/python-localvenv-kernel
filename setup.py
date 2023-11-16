import os
import shutil
import sys
from glob import glob
from pathlib import Path

from setuptools import find_packages, setup

current_dir = os.path.abspath(os.path.dirname(__file__))
setup_args = dict()

# Package the kernel.json file
# Note: this was adapted from the ipython/ipykernel setup.py script
# https://github.com/ipython/ipykernel/blob/abefee4c935ee79d3821dfda02f1511f55d4c996/setup.py#L95
# (Modified BSD License)
if any(a.startswith(("bdist", "install", "develop")) for a in sys.argv):
    sys.path.insert(0, os.path.join(current_dir, "src"))

    spec_dir = Path(current_dir) / "build" / "kernels" / "python-localvenv"
    if spec_dir.is_dir():
        shutil.rmtree(spec_dir)
    spec_dir.mkdir(parents=True)
    from localvenv_kernel.kernelspec import _write_kernelspec

    _write_kernelspec(spec_dir)

    setup_args["data_files"] = [
        # Extract the kernel.json file relative to the installation root
        # (i.e., the virtual environment or system Python installation).
        (
            os.path.join("share", "jupyter", "kernels", "python-localvenv"),
            [str(f) for f in spec_dir.glob("*")],
        ),
    ]
# NOTE: Editable installs won't copy the kernel file. See `Makefile`

with open(os.path.join(current_dir, "README.md")) as fp:
    README = fp.read()

setup(
    name="python-localvenv-kernel",
    version="0.1.4",
    author="Michael H. Goerz",
    author_email="mail@michaelgoerz.net",
    url="https://github.com/goerz/python-localvenv-kernel",
    license="MIT",
    description=(
        "Python Jupyter kernel delegating to a local virtual environment"
    ),
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=["Interactive", "Interpreter", "Shell", "Web"],
    classifiers=[
        "Framework :: Jupyter",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "colorama ~= 0.4.4",
    ],
    **setup_args,
)
