"""
Exercise 3: This exercise is a continuation of the previous one. Implement a simple Decrypt-then-MAC scheme. Test you scheme on some (ciphertext, tag)-pairs that you generated in the previous exercise.
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

# In decrypt-then-MAC, first we check tag. 
# If tag is valid, we proceed with the decryption

# We can also check with a random ciphertext, 
# this should be detected by the MAC.
ciphertext = urandom(len(ciphertext))

result = verifyTag(ciphertext, tag, keyMAC)

if result == True:
    # Tag is valid, proceed with decryption
    decryptedPlaintext = decrypt(ciphertext, keyCipher, nonce)
    print("Tag valid!")
    print("Decrypted plaintext: ", decryptedPlaintext.decode())
else:
    # Tag is invalid, don't decrypt
    print("Tag invalid!")