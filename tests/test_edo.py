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
    assert len(url.path) == 6


def test_batch_shorten(client):
    rv = post_json(
        client, '/api/shorten-batch',
        {'long_urls': [
            'http://www.example.com/1',
            'http://www.example.com/2',
        ]})
    assert rv.status_code == 200
    resp = json.loads(rv.data)
    assert len(resp['links']) == 2
    assert all(urlsplit(l).netloc == edo.app.config['DOMAIN'] for l in resp['links'])


def test_link_should_redirect_to_long_url(client):
    resp = shorten(client, 'http://www.example.com')
    url = urlsplit(resp['link'])
    rv = client.get(url.path)
    assert rv.status_code == 302
    assert rv.headers['Location'] == 'http://www.example.com'


def test_link_with_channel_should_redirect_to_long_url(client):
    resp = shorten(client, 'http://www.example.com')
    url = urlsplit(resp['link'])
    path = url.path + '/foo'
    rv = client.get(path)
    assert rv.status_code == 302
    assert rv.headers['Location'] == 'http://www.example.com'


def test_get_clicks_api(client):
    resp = shorten(client, 'http://www.example.com')
    url = urlsplit(resp['link'])
    linkhash = url.path.split('/')[-1]

    rv = client.get('/api/link/clicks/{}'.format(linkhash))
    resp = json.loads(rv.data)
    assert resp == {'channels': {}, 'total': {'clicks': 0}}
