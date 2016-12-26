from flask import request, jsonify, abort, redirect

from . import app
from .models import db, Link


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
    links = []
    for url in req['long_urls']:
        links.append(Link.shorten(url, commit=False))
    db.session.commit()

    resp = {'links': [l.url for l in links]}
    return jsonify(resp)


@app.route('/<linkhash>')
def visit(linkhash):
    link = Link.get_by_hash(linkhash)
    if not link:
        abort(404)

    return redirect(link.long_url)
