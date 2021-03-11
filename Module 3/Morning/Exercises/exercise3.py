"""
Exercise 3: Generate a random ciphertext and decrypt it using the same key and nonce as in the previous exercise. Does it work? Why/why not?
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

# Try to decrypt a random ciphertext
randomCiphertext = urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), default_backend())
decryptor = cipher.decryptor()
decryptedPlaintext = decryptor.update(randomCiphertext) + decryptor.finalize()
print(decryptedPlaintext)