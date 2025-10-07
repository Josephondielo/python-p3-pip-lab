import sys
import requests
import pytest

def python_version():
    return sys.version_info  # must return the version_info object

def requests_version():
    return requests.__version__

def pytest_version():
    return pytest.__version__
