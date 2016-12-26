from flask_sqlalchemy import SQLAlchemy

from . import app
from .utils import int_to_b64, b64_to_int

db = SQLAlchemy(app)


class Link(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(255))

    @property
    def url(self):
        return 'http://{}/{}'.format(app.config['DOMAIN'], int_to_b64(self.id))

    @classmethod
    def shorten(cls, long_url, commit=True):
        """Shorten a long url, return a Link object."""
        link = cls(long_url=long_url)
        db.session.add(link)
        if commit:
            db.session.commit()
        return link

    @classmethod
    def get_by_hash(cls, linkhash):
        id = b64_to_int(linkhash)
        link = cls.query.filter_by(id=id).first()
        return link
