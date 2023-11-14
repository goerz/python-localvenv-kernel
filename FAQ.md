# Frequently Asked Questions

## Why do I have to install `ipykernel` manually?

Virtual environments should be reproducible. We will not modify the project environment in any way.


## How can I change the directory for the virtual environment?

Currently, the virtual environment has to be in a `.venv` folder. In future versions, we will allow to change this via an environment variable.


## How does this kernel differ from poetry-kernel?

The `python-localvenv-kernel` is derived from the [`poetry-kernel`](https://github.com/pathbird/poetry-kernel). However, instead of delegating to whatever virtual environment Poetry has set up for a project, `python-localvenv-kernel` always delegates to a virtual environment in the `.venv` subdirectory of the project folder.

Thus, `python-localvenv-kernel` does not depend on Poetry. The `.venv` directory could be set up with a simple `python -m venv .venv` and initialized with `pip` based on a `requirements.txt`.

If Poetry's [`virtualenvs.in-project`](https://python-poetry.org/docs/configuration/#virtualenvsin-project) option is set to `true`, Poetry will use a local `.venv` folder for its virtual environment. In that case, the `python-localvenv-kernel` is a *replacement* for `poetry-kernel`. If Poetry is set up to create virtual environments in its [cache directory](https://python-poetry.org/docs/configuration/#cache-directory), the `poetry-kernel` would still be required to run it.

