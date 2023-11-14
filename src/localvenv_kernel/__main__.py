import platform
import signal
import subprocess
import sys
from pathlib import Path

import colorama


def main():
    colorama.init()

    name = ".venv"
    venv_folder = find_venv(name)
    if venv_folder is None:
        error(
            """Cannot start python-localvenv kernel:
                expected folder {venv_name} in notebook directory
                (or any parent directory)
            """,
            f"Couldn't find a virtual environment {name}",
        )
    python = venv_folder / "bin" / "python"
    # TODO: ensure that python exists
    cmd = [
        python,
        "-m",
        "ipykernel_launcher",
        *sys.argv[1:],
    ]
    # TODO: test "python -m ipykernel_launcher --version"
    print(
        colorama.Fore.GREEN
        + "PYTHON-LOCALVENV KERNEL"
        + colorama.Style.RESET_ALL
        + " delegate to "
        + " ".join([str(part) for part in cmd]),
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
        print("ipykernel_launcher exited", file=sys.stderr)
    else:
        print(
            "ipykernel_launcher exited with error code:",
            exit_code,
            file=sys.stderr,
        )


def error(msg, reason):
    print(
        colorama.Fore.RED
        + colorama.Style.BRIGHT
        + +"\n"
        + "!" * 80
        + "\n"
        + msg
        + "\n"
        + "!" * 80
        + "\n"
        + colorama.Style.RESET_ALL,
        file=sys.stderr,
    )
    raise RuntimeError(f"Cannot start python-localvenv kernel: {reason}")


def find_venv(name):
    cwd = Path().resolve()
    candidate_dirs = [cwd, *cwd.parents]
    for dirs in candidate_dirs:
        venv_folder = dirs / name
        if venv_folder.is_dir():
            return venv_folder
    return None


if __name__ == "__main__":
    main()
