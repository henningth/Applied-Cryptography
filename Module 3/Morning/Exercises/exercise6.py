"""
Exercise 6: Continuing from the previous exercise, download the two PDF files from https://shattered.io (Links til en ekstern webside.). Compute the SHA1 hash of each of the two files, what do you observe? What about the MD5 hashes of them?
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

filename1 = "shattered-1.pdf"
with open(filename1, "rb") as f:
    content1 = f.read()

filename2 = "shattered-2.pdf"
with open(filename2, "rb") as f:
    content2 = f.read()

md5digest1 = computeMD5(content1)
sha1digest1 = computeSHA1(content1)
print("MD5(", filename1, "):", md5digest1.hex())
print("SHA1(", filename1, "):", sha1digest1.hex())

md5digest2 = computeMD5(content2)
sha1digest2 = computeSHA1(content2)
print("MD5(", filename2, "):", md5digest2.hex())
print("SHA1(", filename2, "):", sha1digest2.hex())