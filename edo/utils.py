import string

import mmh3

BASE64_ALPHABET = string.ascii_uppercase + string.ascii_lowercase + string.digits + '-_'
BASE64_ALPHABET_REVERSE = {c: i for i, c in enumerate(BASE64_ALPHABET)}



def int30_to_b64(n):
    s = []
    for i in range(5):
        n, r = divmod(n, 64)
        s.append(BASE64_ALPHABET[r])
    assert n == 0
    return ''.join(reversed(s))


def int_to_b64(n):
    s = []
    while n:
        n, r = divmod(n, 64)
        s.append(BASE64_ALPHABET[r])
    return ''.join(reversed(s))


def b64_to_int(s):
    n = 0
    for c in s:
        n = n * 64 + BASE64_ALPHABET_REVERSE[c]
    return n


def hash30(s):
    """Hash string to a 30-bit unsigned integer."""
    return mmh3.hash(s) & 0x3fffffff
