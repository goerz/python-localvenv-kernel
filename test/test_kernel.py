import unittest
import jupyter_kernel_test as jkt
from os.path import sep

# Using test suite from https://github.com/jupyter/jupyter_kernel_test

# This test file must be run from a "site" Python environment that has the
# packages listed in `requirements-site.txt` as well as the
# `python-localvenv-kernel` package. The environment variable
# `KERNEL_VENV=.local-venv` must be set.
#
# Furthermore, the project root must contain a folder `.local-venv` that  has
# the packages listed in `requirements-local.txt` (most importantly,
# `ipykernel`)
#
# On a Unix system, running `make test` from the project root should do the
# right thing. See the `Makefile` for details, or the CI Github workflow.
#
# This only tests the "happy path". Feel free to play around with what happens
# if the `.local-venv` environment doesn't exist, or if `ipykernel` is removed
# from the `.local-venv` environment.


class LocalVenvKernelTests(jkt.KernelTests):
    kernel_name = "python-localvenv"
    language_name = "python"

    # Code in the kernel's language to write "hello, world" to stdout
    code_hello_world = "print('hello, world')"

    def test_localvenv_kernel_module_location(self):
        self.flush_channels()
        # We check that the `sympy` package (which should not be present in
        # the "site" environment) is loaded from the project virtual
        # environment (`.local-venv` in the project root)
        reply, output_msgs = self.execute_helper(
            code="import sympy; sympy.__file__"
        )
        output = output_msgs[0]["content"]["data"]["text/plain"]
        self.assertTrue(f"{sep}.local-venv{sep}" in output)
        self.assertFalse(f"{sep}.site-venv{sep}" in output)


if __name__ == "__main__":
    unittest.main()
