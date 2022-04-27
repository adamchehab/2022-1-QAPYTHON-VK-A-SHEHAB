import os
import signal
import subprocess
import time

from copy import copy
import requests
import settings


from requests.exceptions import ConnectionError


repo_root = os.path.abspath(os.path.join(__file__, os.pardir))


def wait_ready():
    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f"http://{settings.APP_HOST}:{settings.APP_PORT}")
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError("App did not start in 5s!")


def pytest_configure(config):
    if not hasattr(config, "workerinput"):
        app_path = os.path.join(repo_root, "application", "app.py")

        env = copy(os.environ)
        env.update(
            {
                "APP_HOST": settings.APP_HOST,
                "APP_PORT": settings.APP_PORT,
            }
        )

        # app_stderr = open("/tmp/app_stderr", "w")
        # app_stdout = open("/tmp/app_stdout", "w")

        app_stderr = open(os.path.join(repo_root, "tmp", "app_stderr"), "w")
        app_stdout = open(os.path.join(repo_root, "tmp", "app_stdout"), "w")

        app_proc = subprocess.Popen(
            ["python3.8", app_path],
            stderr=app_stderr,
            stdout=app_stdout,
            env=env
        )
        wait_ready()

        config.app_proc = app_proc
        config.app_stderr = app_stderr
        config.app_stdout = app_stdout


def pytest_unconfigure(config):
    config.app_proc.send_signal(signal.SIGINT)
    exit_code = config.app_proc.wait()

    assert exit_code == 0, f"app exited abnormally with code: {exit_code}"

    config.app_stderr.close()
    config.app_stdout.close()
