.PHONY: help clean install develop uninstall

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

clean:   ## Remove all build and compilation artifacts
	rm -rf build
	rm -rf dist
	rm -rf python_localvenv_kernel.egg-info
	rm -rf src/localvenv_kernel/__pycache__
