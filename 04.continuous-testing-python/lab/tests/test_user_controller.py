# lab/tests/test_user_controller.py
"""
import pytest
from lab.src.controllers import user as user_controller
from lab.src import dbclient

@pytest.fixture(autouse=True)
def run_around_tests():
    dbclient.flushdb()
    yield
    dbclient.flushdb()

def test_create_user_success():
    user = {"username":"sergkudinov","firstname":"Sergei","lastname":"Kudinov"}
    result, err = user_controller.create(user)
    assert err is None
    assert result == "OK"

def test_create_user_missing_username():
    user = {"firstname":"Sergei","lastname":"Kudinov"}
    result, err = user_controller.create(user)
    assert err is not None
    assert result is None

def test_get_user_success():
    user = {"username":"sergkudinov","firstname":"Sergei","lastname":"Kudinov"}
    res, err = user_controller.create(user)
    assert err is None
    retrieved, err = user_controller.get("sergkudinov")
    assert err is None
    assert retrieved == user

def test_get_user_not_found():
    retrieved, err = user_controller.get("unknownuser")
    assert err is not None
    assert retrieved is None

    """