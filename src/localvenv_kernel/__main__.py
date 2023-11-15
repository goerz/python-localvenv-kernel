import os
import platform
import signal
import subprocess
import sys
from textwrap import dedent
from pathlib import Path

import colorama


def main():
    colorama.init()

    # The working directory (cwd) is always the folder that contains the
    # notebook. This may be a subfolder of the directory in which the Jupyter
    # server was started.
    cwd = Path().resolve()
    name = os.environ.get("KERNEL_VENV", ".venv").strip()
    venv_folder = find_venv(cwd, name)
    if venv_folder is None:
        if os.path.isabs(name):
            error(
                f"""
                Expected folder KERNEL_VENV="{name}" to exist
                """
            )
        else:
            error(
                f"""
                Expected folder "{name}" in notebook directory {cwd}
                (or any parent directory)
                """
            )
    python = find_python(venv_folder)
    cmd_check_kernel = [
        python,
        "-m",
        "ipykernel_launcher",
        "--version",
    ]
    try:
        kernel_version = subprocess.check_output(
            cmd_check_kernel, stderr=subprocess.STDOUT, text=True
        )
    except subprocess.CalledProcessError as exc_info:
        error(
            f"""
            {' '.join([str(a) for a in cmd_check_kernel])}
            returned exit status {exc_info.returncode}

            ERROR: {exc_info.output.strip()}

            Make sure that the 'ipykernel' package is installed in the virtual
            environment {venv_folder}
            """
        )
    cmd = [
        python,
        "-m",
        "ipykernel_launcher",
        *sys.argv[1:],
    ]
    print(
        colorama.Fore.GREEN
        + "PYTHON-LOCALVENV KERNEL"
        + colorama.Style.RESET_ALL
        + " delegate to "
        + " ".join([str(part) for part in cmd])
        + f" (version {kernel_version.strip()})",
        file=sys.stderr,
    )
    proc = subprocess.Popen(cmd)

    if platform.system() == "Windows":
        forward_signals = set(signal.Signals) - {
            signal.CTRL_BREAK_EVENT,
            signal.CTRL_C_EVENT,
            signal.SIGTERM,
        }
    else:
        forward_signals = set(signal.Signals) - {
            signal.SIGKILL,
            signal.SIGSTOP,
        }

    def handle_signal(sig, _frame):
        proc.send_signal(sig)

    for sig in forward_signals:
        signal.signal(sig, handle_signal)

    exit_code = proc.wait()
    if exit_code == 0:
        print(
            "PYTHON-LOCALVENV KERNEL: ipykernel_launcher exited",
            file=sys.stderr,
        )
    else:
        print(
            "PYTHON-LOCALVENV KERNEL: ipykernel_launcher exited with code:",
            exit_code,
            file=sys.stderr,
        )


def error(msg):
    print(
        colorama.Fore.RED
        + colorama.Style.BRIGHT
        + "\n"
        + "!" * 80
        + "\nCannot start python-localvenv kernel:\n"
        + dedent(msg)
        + "!" * 80
        + "\n"
        + colorama.Style.RESET_ALL,
        file=sys.stderr,
    )
    sys.exit(1)


def find_venv(root, name):
    candidate_dirs = [root, *root.parents]
    if os.path.isabs(name) and os.path.isdir(name):
        return Path(name)
    else:
        for dirs in candidate_dirs:
            venv_folder = dirs / name
            if venv_folder.is_dir():
                return venv_folder
    return None


def find_python(venv):
    if "KERNEL_VENV_PYTHON" in os.environ:
        python = venv / os.path.normpath(os.environ["KERNEL_VENV_PYTHON"])
    else:
        python = venv / "bin" / "python"
        if platform.system() == "Windows":
            python = venv / "Scripts" / "python"
    return python


if __name__ == "__main__":
    main()
