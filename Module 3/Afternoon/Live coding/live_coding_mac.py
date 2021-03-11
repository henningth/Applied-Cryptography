"""
Compute and validate MAC of some data
"""

from cryptography.hazmat.primitives import hashes, hmac
from cryptography.exceptions import InvalidSignature
from os import urandom

def computeTag(message, key):
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(message)
    tag = h.finalize()
    return tag

def verifyTag(message, tag, key):
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(message)
    try:
        h.verify(tag)
        return True
    except InvalidSignature:
        return False

# Compute tag of message
key = urandom(16)
message = b'Yellow Submarine'
tag = computeTag(message, key)
print("Tag of message", message.decode(), "is", tag.hex())

# Verify tag
result = verifyTag(message, tag, key)
print(result)

# Try with a different message
newMessage = b'Yellow submarine'
newTag = computeTag(newMessage, key)
print("Tag of message", newMessage.decode(), "is", newTag.hex())

newResult = verifyTag(newMessage, tag, key)
print(newResult)