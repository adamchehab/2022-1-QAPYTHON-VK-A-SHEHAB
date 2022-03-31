import os
import shutil
import sys

from ui.fixtures import *


@pytest.fixture(scope='session')
def base_temp_dir():
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    return base_dir


@pytest.fixture(scope='function')
def temp_dir(base_temp_dir, request):
    test_dir = os.path.join(base_temp_dir, request._pyfuncitem.nodeid)
    os.makedirs(test_dir)
    return test_dir
