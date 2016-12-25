import string

BASE64_ALPHABET = string.ascii_uppercase + string.ascii_lowercase + string.digits + '-_'
BASE64_ALPHABET_REVERSE = {c: i for i, c in enumerate(BASE64_ALPHABET)}


def int_to_b64(n):
    s = []
    while n:
        n, r = divmod(n, 64)
        s.append(BASE64_ALPHABET[r])
    return ''.join(s)


def b64_to_int(s):
    n = 0
    for c in s:
        n = n * 64 + BASE64_ALPHABET_REVERSE[c]
    return n
