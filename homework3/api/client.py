import requests
from utils.utils import random_str


class ApiClient:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.csrf = None
        self.segment_id = None
        self.session = requests.Session()

    def post_login(self):
        headers = {
            'Referer': 'https://target.my.com/',
        }

        data = {
            'email': self.login,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }

        resp = self.session.post(
            url='https://auth-ac.my.com/auth?lang=ru&nosavelogin=0',
            data=data,
            headers=headers,
            allow_redirects=True
        )
        self.csrf = self.session.get(url='https://target.my.com/csrf/').cookies.get('csrftoken')

        return resp

    def post_segment(self):
        headers = {
            'X-CSRFToken': self.csrf
        }

        json = {
            "name": random_str(8),
            "pass_condition": 1,
            "relations": [
                {
                    "object_type": "remarketing_player",
                    "params": {
                        "type": "positive",
                        "left": 365,
                        "right": 0
                    }
                }
            ],
            "logicType": "or"
        }

        resp = self.session.post(
            url='https://target.my.com/api/v2/remarketing/segments.json',
            json=json,
            headers=headers
        )

        self.segment_id = resp.json()['id']
        return resp

    def delete_segment(self):
        headers = {
            'X-CSRFToken': self.csrf
        }

        resp = self.session.delete(
            url=f'https://target.my.com/api/v2/remarketing/segments/{self.segment_id}.json',
            headers=headers
        )

        return resp

    def check_segment(self):
        headers = {
            'X-CSRFToken': self.csrf
        }

        resp = self.session.get(
            url=f'https://target.my.com/api/v2/remarketing/segments/{self.segment_id}.json',
            headers=headers
        )

        return resp
