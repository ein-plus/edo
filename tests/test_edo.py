import json
from urllib.parse import urlsplit

import pytest

import edo


@pytest.fixture
def client(request):
    edo.app.config['TESTING'] = True
    client = edo.app.test_client()
    yield client


def post_json(client, path, data):
    return client.post(path, data=json.dumps(data), content_type='application/json')


def test_shorten(client):
    rv = post_json(client, "/api/shorten",
                   {"long_url": "http://www.example.com"})
    assert rv.status_code == 200
    resp = json.loads(rv.data)
    url = urlsplit(resp['link'])
    assert url.scheme == 'http'
    assert url.netloc == edo.app.config['DOMAIN']
    assert len(url.path) == 6 and url.path[0] == '/'
