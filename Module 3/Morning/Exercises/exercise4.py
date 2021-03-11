"""
Exercise 4: Starting from the first live-coding today (about MD5 and SHA1), add functionality so that the user can enter a string, which the program then computes and displays the MD5 and SHA1 hashes of. Test with strings that are similar, such as “Hello” and “H3llo”.
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

message = input("Enter string to compute MD5 and SHA1 hash of: ").encode()
md5digest = computeMD5(message)
sha1digest = computeSHA1(message)
print("MD5(", message, "):", md5digest.hex())
print("SHA1(", message, "):", sha1digest.hex())