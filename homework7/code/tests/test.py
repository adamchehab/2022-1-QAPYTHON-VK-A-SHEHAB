import requests
import settings


url = f"http://{settings.APP_HOST}:{settings.APP_PORT}"


# def test():
#     print(requests.get(url).text)


def test_add_get_user():
    resp = requests.post(f"{url}/add_user", json={"name": "Ilya"})
    user_id_from_add = resp.json()["user_id"]

    resp = requests.get(f"{url}/get_user/Ilya")
    user_id_from_get = resp.json()["user_id"]

    assert user_id_from_add == user_id_from_get


def test_add_existent_user():
    requests.post(f"{url}/add_user", json={"name": "Vasya"})
    resp = requests.post(f"{url}/add_user", json={"name": "Vasya"})
    assert resp.status_code == 400


def test_get_non_existent_user():
    resp = requests.get(f"{url}/Masha")
    assert resp.status_code == 404
