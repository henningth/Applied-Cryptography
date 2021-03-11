"""
Live coding with MD5 and SHA1 hash functions.

Testing with text strings.

Testing for avalanche effect.
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

message = b'Yellow Submarine'
message2 = b' diving'

# Compute MD5 hash of a string
md5digest = hashes.Hash(hashes.MD5(), default_backend())
md5digest.update(message)
md5digest.update(message2)
md5hash = md5digest.finalize()
print(md5hash.hex())

# Note: When using update, the previous data is overwritten
message3 = b'Yellow Submarine diving'
md5digest3 = hashes.Hash(hashes.MD5(), default_backend())
md5digest3.update(message)
md5hash2 = md5digest3.finalize()
print(md5hash2.hex())

# Compute the SHA1 hash of a string
sha1digest = hashes.Hash(hashes.SHA1(), default_backend())
sha1digest.update(message3)
sha1hash = sha1digest.finalize()
print(sha1hash.hex())

# Test for the avalanche effect
message4 = b'Yellow Submarine Diving'
sha1digest = hashes.Hash(hashes.SHA1(), default_backend())
sha1digest.update(message4)
sha1hash = sha1digest.finalize()
print(sha1hash.hex())
