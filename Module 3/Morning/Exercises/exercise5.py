"""
Exercise 5: Starting from the first live-coding today (about MD5 and SHA1), compute the MD5 and SHA1 hash of a file or your choosing. Have the program print the filename as well as the MD5 and SHA1 hashes of it.
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def computeMD5(message):
    md5hash = hashes.Hash(hashes.MD5(), default_backend())
    md5hash.update(message)
    md5digest = md5hash.finalize()
    return md5digest

def computeSHA1(message):
    sha1hash = hashes.Hash(hashes.SHA1(), default_backend())
    sha1hash.update(message)
    sha1digest = sha1hash.finalize()
    return sha1digest

filename = "Dice.png"
with open(filename, "rb") as f:
    content = f.read()

md5digest = computeMD5(content)
sha1digest = computeSHA1(content)
print("MD5(", filename, "):", md5digest.hex())
print("SHA1(", filename, "):", sha1digest.hex())