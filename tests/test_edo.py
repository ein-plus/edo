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


def shorten(client, url):
    rv = post_json(client, "/api/shorten", {"long_url": url})
    assert rv.status_code == 200
    return json.loads(rv.data)


def test_shorten(client):
    resp = shorten(client, 'http://www.example.com')
    url = urlsplit(resp['link'])
    assert url.scheme == 'http'
    assert url.netloc == edo.app.config['DOMAIN']
    assert len(url.path) <= 6


def test_link_should_redirect_to_long_url(client):
    resp = shorten(client, 'http://www.example.com')
    url = urlsplit(resp['link'])
    rv = client.get(url.path)
    assert rv.status_code == 302
    assert rv.headers['Location'] == 'http://www.example.com'
