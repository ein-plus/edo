from flask import request, jsonify, abort, redirect

from . import app
from .models import Link


@app.route('/api/shorten', methods=['POST'])
def shorten():
    req = request.get_json()
    long_url = req['long_url']

    link = Link.shorten(long_url)

    resp = {'link': link.url}
    return jsonify(resp)


@app.route('/api/shorten-batch', methods=['POST'])
def shorten_batch():
    req = request.get_json()
    links = Link.shorten_batch(req['long_urls'])
    resp = {'links': [l.url for l in links]}
    return jsonify(resp)


@app.route('/<linkhash>', defaults={'channel': None})
@app.route('/<linkhash>/<channel>')
def visit(linkhash, channel):
    link = Link.get_by_hash(linkhash)
    if not link:
        abort(404)

    return redirect(link.long_url)
