# nukeuuid py.test configuration
import pytest


@pytest.fixture(scope='session')
def nuke():
    import nuke
    return nuke


@pytest.fixture(scope='session')
def nukeuuid():
    import nukeuuid
    return nukeuuid


@pytest.fixture(scope='session')
def uuid():
    import uuid
    return uuid
