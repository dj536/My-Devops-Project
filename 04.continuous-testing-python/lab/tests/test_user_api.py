# lab/tests/test_user_api.py
from fastapi.testclient import TestClient
from lab.src.app import app
from lab.src import dbclient

client = TestClient(app)

def setup_function():
    dbclient.flushdb()

def teardown_module(module):
    # nothing to close in this simplified setup
    pass

def test_post_create_user_success():
    user = {"username":"sergkudinov","firstname":"Sergei","lastname":"Kudinov"}
    res = client.post("/user/", json=user)
    assert res.status_code == 201
    assert res.json().get("status") == "success"

def test_post_create_user_bad_request():
    user = {"firstname":"Sergei","lastname":"Kudinov"}
    res = client.post("/user/", json=user)
    assert res.status_code == 400

def test_get_user_success():
    user = {"username":"alice","firstname":"Alice","lastname":"Doe"}
    client.post("/user/", json=user)
    res = client.get("/user/alice")
    assert res.status_code == 200
    assert res.json().get("username") == "alice"

def test_get_user_not_found():
    res = client.get("/user/unknown")
    assert res.status_code == 404