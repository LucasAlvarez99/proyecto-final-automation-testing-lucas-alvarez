import requests

BASE = "https://reqres.in/api"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def test_get_users():
    r = requests.get(f"{BASE}/users?page=2", headers=HEADERS)
    assert r.status_code == 200
    body = r.json()
    assert "data" in body
    assert isinstance(body["data"], list)

def test_create_user_and_delete():
    payload = {"name": "morpheus", "job": "leader"}
    r = requests.post(f"{BASE}/users", json=payload, headers=HEADERS)
    assert r.status_code == 201
    data = r.json()
    user_id = data.get("id")
    assert user_id is not None

    # delete (reqres solo simula la eliminación)
    r2 = requests.delete(f"{BASE}/users/{user_id}", headers=HEADERS)
    assert r2.status_code in (204, 200, 202)

def test_get_single_user_not_found():
    r = requests.get(f"{BASE}/users/23", headers=HEADERS)
    assert r.status_code == 404