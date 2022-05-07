import pytest
from api.client import ApiClient

CREDENTIALS = ['adamchehab@gmail.com', 'password123']


@pytest.mark.API
class TestSegments:

    def test_segment_create(self):
        client = ApiClient(*CREDENTIALS)
        client.post_login()
        assert client.post_segment().status_code == 200
        assert client.check_segment().status_code == 200
        client.delete_segment()

    def test_segment_delete(self):
        client = ApiClient(*CREDENTIALS)
        client.post_login()
        client.post_segment()
        assert client.delete_segment().status_code == 204
        assert client.check_segment().status_code == 404
