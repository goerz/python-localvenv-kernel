.PHONY: help clean install develop uninstall build test

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
    match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
    if match:
        target, help = match.groups()
        print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


define DEVELOP_KERNEL_INSTALL_PYSCRIPT
import sys
import shutil
from pathlib import Path
src = Path("build") / "kernels"
dst = Path(sys.prefix) / "share" / "jupyter" / "kernels"
shutil.copytree(src, dst, dirs_exist_ok=True)
endef
export DEVELOP_KERNEL_INSTALL_PYSCRIPT


define DEVELOP_KERNEL_UNINSTALL_PYSCRIPT
import sys
import shutil
from pathlib import Path
kernel = Path(sys.prefix) / "share" / "jupyter" / "kernels" / "python-localvenv"
if kernel.is_dir():
    print(f'Removing "{kernel}"')
    shutil.rmtree(kernel)
endef
export DEVELOP_KERNEL_UNINSTALL_PYSCRIPT


PYTHON ?= python3

help:   ## Show this help
	@$(PYTHON) -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

install:  ## Install the package into the current PYTHON installation with pip
	@$(PYTHON) -m pip install .

develop:  ## Dev-install the package into the current PYTHON installation with pip
	@$(PYTHON) -m pip install -e .
	@$(PYTHON) -c "$$DEVELOP_KERNEL_INSTALL_PYSCRIPT"

uninstall:  ## Uninstall package installed with `make install` or `make develop`
	@$(PYTHON) -m pip uninstall python-localvenv-kernel
	@$(PYTHON) -c "$$DEVELOP_KERNEL_UNINSTALL_PYSCRIPT"

build: ## Locally build package (source distribution and wheel)
	$(PYTHON) -m build --no-isolation

.site-venv/bin/python:
	$(PYTHON) -m venv .site-venv
	PIP_DISABLE_PIP_VERSION_CHECK=1 .site-venv/bin/python -m pip install -r test/requirements-site.txt
	PIP_DISABLE_PIP_VERSION_CHECK=1 .site-venv/bin/python -m pip install -e .
	.site-venv/bin/python -c "$$DEVELOP_KERNEL_INSTALL_PYSCRIPT"

.local-venv/bin/python:
	$(PYTHON) -m venv .local-venv
	PIP_DISABLE_PIP_VERSION_CHECK=1 .local-venv/bin/python -m pip install -r test/requirements-local.txt

test: .site-venv/bin/python .local-venv/bin/python  ## Test the kernel
	KERNEL_VENV=.local-venv .site-venv/bin/python test/test_kernel.py

codestyle:  ## Auto-format the code
	black --line-length 79 .

clean:   ## Remove all build and compilation artifacts
	rm -rf build
	rm -rf dist
	rm -rf python_localvenv_kernel.egg-info
	rm -rf src/localvenv_kernel/__pycache__
	rm -rf test/__pycache__
	rm -rf .site-venv
	rm -rf .local-venv
