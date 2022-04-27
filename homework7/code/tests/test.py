import requests
import settings


url = f"http://{settings.APP_HOST}:{settings.APP_PORT}"


def test():
    print(requests.get(url).text)
