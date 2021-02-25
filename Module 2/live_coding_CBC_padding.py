"""
Live coding CBC with padding
"""

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

key = os.urandom(16)
iv = os.urandom(16)

cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CBC(iv), backend=default_backend())

# Encryption
plaintext = b"Yellow Submari"

padder = padding.PKCS7(128).padder()

paddedPlaintext = padder.update(plaintext) + padder.finalize()

print(paddedPlaintext)

encryptor = cipher.encryptor()
ciphertext = encryptor.update(paddedPlaintext) + encryptor.finalize()
print(ciphertext)

# Decryption
decryptor = cipher.decryptor()
decryptedCiphertext = decryptor.update(ciphertext) + decryptor.finalize()
print(decryptedCiphertext)

unpadder = padding.PKCS7(128).unpadder()
unpaddedDecryptedCiphertext = unpadder.update(decryptedCiphertext) + unpadder.finalize()

print(unpaddedDecryptedCiphertext)