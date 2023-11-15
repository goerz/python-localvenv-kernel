# Frequently Asked Questions

## Why do I have to install `ipykernel` manually?

Virtual environments should be reproducible. We will not modify the project environment in any way.

## The "Python (local .venv)" kernel does not show up in Jupyter

The `python-localvenv-kernl` must be installed in the same environment as `jupyter`. Run `jupyter kernelspec list`. This should show something like

```
…
python-localvenv     {sys.prefix}/share/jupyter/kernels/python-localvenv
python3              {sys.prefix}/share/jupyter/kernels/python3
```

where `{sys.prefix}` is the path to the environment where `jupyter` is installed. The `python3` kernel on the last line is the default kernel for that Jupyter installation. If `python-localvenv` is not listed with the same `{sys.prefix}`, the package is not installed correctly. Run

```
./bin/python -m pip install python-localvenv-kernel
```

inside the `{sys.prefix}` folder (or, if the `{sys.prefix}` folder is managed by `conda`, use `conda install python-localvenv-kernel` as appropriate) to install the package into the environment.


## How can I change the directory for the virtual environment?

Setting the environment variable `KERNEL_VENV` allows to override the folder name for the project virtual environment. The `python-localvenv-kernel` will search for the folder name in the directory where the notebook file is located and all its parent directories.

Setting `KERNEL_VENV` to an absolute path will use that path directly. In all cases, the `KERNEL_VENV` must point to a Python environment (`{KERNEL_VENV}/bin/python` must exist) and that environment must have the `ipykernel` package installed.


## How does this kernel differ from poetry-kernel?

The `python-localvenv-kernel` is derived from the [`poetry-kernel`](https://github.com/pathbird/poetry-kernel). However, instead of delegating to whatever virtual environment Poetry has set up for a project, `python-localvenv-kernel` always delegates to a virtual environment in the `.venv` subdirectory of the project folder (respectively, the directory pointed to by the `KERNEL_VENV` environment variable).

Thus, `python-localvenv-kernel` does not depend on Poetry. The `.venv` directory could be set up with a simple `python -m venv .venv` and initialized with `pip` based on a `requirements.txt`.

If Poetry's [`virtualenvs.in-project`](https://python-poetry.org/docs/configuration/#virtualenvsin-project) option is set to `true`, Poetry will use a local `.venv` folder for its virtual environment. In that case, the `python-localvenv-kernel` is a *replacement* for `poetry-kernel`. If instead, Poetry is set up to create virtual environments in its [cache directory](https://python-poetry.org/docs/configuration/#cache-directory), using the `poetry-kernel` might be more appropriate. However, even in that case, `python-locavenv-kernel` could still be used, by setting the environment variable

~~~
KERNEL_VENV=`poetry env info -p`
~~~

immediately before launching `jupyter` from the project directory.
