from flask_sqlalchemy import SQLAlchemy

from . import app
from .utils import int_to_b64, int30_to_b64, b64_to_int, hash30

db = SQLAlchemy(app)


class Link(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    hash_ = db.Column('hash', db.Integer)
    long_url = db.Column(db.String(255))
    clicks = db.relationship('Click', backref='link', lazy='dynamic')

    @property
    def url(self):
        return 'http://{}/{}'.format(app.config['DOMAIN'], int30_to_b64(self.hash_))

    @classmethod
    def shorten(cls, long_url, commit=True):
        """Shorten a long url, return a Link object."""
        # FIXME: resolve hash conflict!
        hash_ = hash30(long_url)
        link = cls.query.filter_by(hash_=hash_).first()
        if link:
            return link

        link = cls(long_url=long_url, hash_=hash_)
        db.session.add(link)
        if commit:
            db.session.commit()
        return link

    @classmethod
    def shorten_batch(cls, long_urls):
        links = []
        for url in long_urls:
            link = cls.shorten(url, commit=False)
            links.append(link)

        db.session.commit()
        return links

    @classmethod
    def get_by_hash(cls, linkhash):
        hash_ = b64_to_int(linkhash)
        link = cls.query.filter_by(hash_=hash_).first()
        return link


class Click(db.Model):
    __tablename__ = 'clicks'

    id = db.Column(db.Integer, primary_key=True)
    link_id = db.Column(db.Integer, db.ForeignKey('links.id'))
    channel_id = db.Column(db.Integer)
    count = db.Column(db.Integer)

    @classmethod
    def gets_by_hash(cls, linkhash):
        link = Link.get_by_hash(linkhash)
        if not link:
            return []

        return link.clicks

    @classmethod
    def record(cls, link, channel):
        # decode channel to integer
        if channel is None:
            channel_id = 0
        else:
            try:
                channel_id = b64_to_int(channel)
            except (ValueError, IndexError):
                channel_id = 0

        db.session.execute(
            "INSERT INTO clicks (link_id, channel_id, count) "
            "VALUES (:link_id, :channel_id, 1) "
            "ON DUPLICATE KEY UPDATE count=count+1",
            {'link_id': link.id, 'channel_id': channel_id})
        db.session.commit()


    @property
    def channel(self):
        if self.channel_id == 0:
            return ''
        else:
            return int_to_b64(self.channel_id)
