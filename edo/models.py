from . import app
from .utils import hash30, int30_to_b64


class Link:
    def __init__(self, hashstr):
        self.url = 'http://{}/{}'.format(app.config['DOMAIN'], hashstr)

    @classmethod
    def shorten(cls, long_url):
        """Shorten a long url, return a Link object."""
        hashint = hash30(long_url)
        hashstr = int30_to_b64(hashint)
        return cls(hashstr)
