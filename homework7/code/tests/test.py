import requests


def test():
    print(requests.get('http://127.0.0.1:5000').text)
