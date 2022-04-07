import pytest
from api.client import ApiClient

CREDENTIALS = ['adamchehab@gmail.com', 'password123']


@pytest.mark.API
class TestSegments:

    def test_segment_create(self):
        client = ApiClient(*CREDENTIALS)
        client.post_login()
        resp = client.post_segment()
        assert resp.status_code == 200
        client.delete_segment()

    def test_segment_delete(self):
        client = ApiClient(*CREDENTIALS)
        client.post_login()
        client.post_segment()
        resp = client.delete_segment()
        assert resp.status_code == 204
