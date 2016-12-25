import string

import pyhash

BASE64_ALPHABET = string.ascii_uppercase + string.ascii_lowercase + string.digits + '-_'

hasher = pyhash.murmur3_32()


def hash30(s):
    return hasher(s) & 0x3fffffff


def int30_to_b64(n):
    s = []
    for i in range(5):
        n, r = divmod(n, 64)
        s.append(BASE64_ALPHABET[r])
    return ''.join(s)
