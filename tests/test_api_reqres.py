import requests

BASE = "https://reqres.in/api"

def test_get_users():
    r = requests.get(f"{BASE}/users?page=2")
    assert r.status_code == 200
    body = r.json()
    assert "data" in body
    assert isinstance(body["data"], list)

def test_create_user_and_delete():
    payload = {"name": "morpheus", "job": "leader"}
    r = requests.post(f"{BASE}/users", json=payload)
    assert r.status_code == 201
    data = r.json()
    user_id = data.get("id")
    assert user_id is not None

    # Delete (reqres fakes deletes but returns 204)
    r2 = requests.delete(f"{BASE}/users/{user_id}")
    assert r2.status_code in (204, 200, 202)

def test_get_single_user_not_found():
    r = requests.get(f"{BASE}/users/23")
    assert r.status_code == 404
