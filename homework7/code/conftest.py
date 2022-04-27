import os
import signal
import subprocess

import time
# from copy import copy
# import requests
# import settings

# from requests.exceptions import ConnectionError


repo_root = os.path.abspath(os.path.join(__file__, os.pardir))


# def wait_app_ready():
#     started = False
#     st = time.time()
#     while time.time() - st <= 10:
#         try:
#             requests.get(f'http://{settings.APP_HOST}:{settings.APP_PORT}')
#             started = True
#             break
#         except ConnectionError:
#             pass

#     if not started:
#         raise RuntimeError('App did not start in 10s')


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        app_path = os.path.join(repo_root, 'application', 'app.py')
        app_proc = subprocess.Popen(['python3.8', app_path])

        # Wait till server starts
        time.sleep(5)

        config.app_proc = app_proc


def pytest_unconfigure(config):
    config.app_proc.send_signal(signal.SIGINT)
    exit_code = config.app_proc.wait()

    assert exit_code == 0, f'app exited abnormally with code: {exit_code}'
