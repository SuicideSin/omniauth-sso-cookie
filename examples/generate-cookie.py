import hashlib
import hmac
import json
import time

from Crypto import Cipher
from Crypto import Random


# Keys must have a length of 256 bits (32 chars)
ENCRYPTION_KEY = 'LXWRMxv84CsXvZVWm2gQ3AKcZf7e7rpR'
HMAC_KEY       = '53HGbrQJLq5iXIhPhU9JM2259WfgqCr6'


def create_cookie(datadict):
    values = json.dumps(datadict, separators=(',',':'))
    pad_value = Cipher.AES.block_size - len(values) % Cipher.AES.block_size;
    values = values + pad_value * chr(pad_value)
    iv = Random.new().read(Cipher.AES.block_size)
    cipher = Cipher.AES.new(ENCRYPTION_KEY, Cipher.AES.MODE_CBC, iv)
    data = iv + cipher.encrypt(values)
    sig = hmac.new(HMAC_KEY, data, hashlib.sha256).digest()
    return (data + sig).encode('base64').replace('\n', '')


print create_cookie({
    'uid': 12345,
    'nickname': 'FizzBuzz',
    'email': 'fizzbuzz@example.com',
    'expires': int(time.time() + 10*24*60*60*10),
})
