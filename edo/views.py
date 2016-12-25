from flask import request, jsonify

from . import app
from .models import Link


@app.route('/api/shorten', methods=['POST'])
def shorten():
    req = request.get_json()
    long_url = req['long_url']

    link = Link.shorten(long_url)

    resp = {'link': link.url}
    return jsonify(resp)
