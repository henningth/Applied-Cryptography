"""
Exercise 2: Starting with the live-coding with the MAC, implement a simple Encrypt-then-MAC scheme. Be sure to use two different keys for the Encryption and MAC respectively. Test your scheme on some plaintexts, and print the resulting ciphertexts and associated MAC tags. Use AES-CTR for encryption and HMAC-SHA256 for the MAC.
"""

from cryptography.hazmat.primitives import hashes, hmac
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
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

def encrypt(plaintext, key, nonce):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

def decrypt(ciphertext, key, nonce):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), default_backend())
    decryptor = cipher.decryptor()
    decryptedPlaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return decryptedPlaintext

# In Encrypt-then-MAC, first we encrypt, then we compute tag of 
# the resulting ciphertext

keyCipher = urandom(16)
keyMAC = urandom(16)
nonce = urandom(16)

plaintext = b'Sydney is in Australia'
ciphertext = encrypt(plaintext, keyCipher, nonce)

tag = computeTag(ciphertext, keyMAC)

print("Ciphertext: ", ciphertext)
print("Tag: ", tag)