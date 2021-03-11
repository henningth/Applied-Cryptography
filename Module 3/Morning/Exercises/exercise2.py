"""
Exercise 2: Begin by encrypting a string of your own choosing using AES-CTR. Then, change one byte in the ciphertext, and try to decrypt this modified ciphertext using the same key as before. Does it work, and if so, what is the (modified?) plaintext?
Also change one byte in the key, can you decrypt using the modified key?
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom

key = urandom(16)
nonce = urandom(16)

newKey = b'\xfa' + key[1:]

# Encrypt the plaintext
plaintext = b'Yellow Submarine'
cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()
print(ciphertext.hex())

# Decrypt the ciphertext
decryptor = cipher.decryptor()
decryptedPlaintext = decryptor.update(ciphertext) + decryptor.finalize()
print(decryptedPlaintext)

# Modify and then decrypt the modified ciphertext
modifiedCiphertext = bytearray()
modifiedCiphertext = b'\xfe' + ciphertext[1:]
print(modifiedCiphertext.hex())
decryptor = cipher.decryptor()
decryptedPlaintext = decryptor.update(modifiedCiphertext) + decryptor.finalize()
print(decryptedPlaintext)

# Try to decrypt with key where one byte is changed in the key
cipher = Cipher(algorithms.AES(newKey), modes.CTR(nonce), default_backend())
decryptor = cipher.decryptor()
decryptedPlaintext = decryptor.update(ciphertext) + decryptor.finalize()
print(decryptedPlaintext)