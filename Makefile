.PHONY: help clean

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

PYTHON ?= python3

help:   ## Show this help
	@$(PYTHON) -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean:   ## Remove all build and compilation artifacts
	rm -rf build
	rm -rf data_kernelspec
	rm -rf python_localvenv_kernel.egg-info
	rm -rf src/localvenv_kernel/__pycache__
