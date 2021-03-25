"""
Write a program in Python which, given some data, computes the following:

The MD5 digest of the data
The SHA256 digest of the data
The HMAC-SHA256 MAC tag of the data

Have the program print the data and the computed digests and MAC tag

Try with some data which is plaintext, what do you observe about the digests and MAC tag?

Continuing from the previous slide, add code that, given data and its associated MAC tag, verifies the tag

Try to change the data without changing the MAC tag, does the verification succeed?

Try to change the MAC tag without changing the data, does the verification succeed?
"""
from os import urandom

from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

data = b'Hello Java World'
print(data.decode())

# Compute MD5 digest of data
md5hash = hashes.Hash(hashes.MD5(), default_backend())
md5hash.update(data)
md5digest = md5hash.finalize()
print("MD5", md5digest.hex())

# Compute SHA256 digest of data
sha256hash = hashes.Hash(hashes.SHA256(), default_backend())
sha256hash.update(data)
sha256digest = sha256hash.finalize()
print("SHA256:", sha256digest.hex())

# Compute HMAC-SHA256 MAC tag of the data
key = urandom(16) # Note that MAC needs a key
hmacsha256 = hmac.HMAC(key, hashes.SHA256(), default_backend())
hmacsha256.update(data)
tag = hmacsha256.finalize()
print("MAC Tag:", tag.hex())

#newTag = bytearray()
#newTag = b'\x43' + tag[1:]
newData = bytearray()
newData = b'\x6e' + data[1:]
print(newData)

# Verify the given MAC tag, given data and tag.
hmacsha256 = hmac.HMAC(key, hashes.SHA256(), default_backend())
hmacsha256.update(newData)
try:
    hmacsha256.verify(tag)
    print("OK")
except InvalidSignature:
    print("FAIL")