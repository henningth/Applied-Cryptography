"""
Live coding AES-CTR
"""

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = os.urandom(16)
nonce = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), default_backend())

# Encryption
plaintext = b'Yellow Submarine'
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()
print(ciphertext)

# Decryption
decryptor = cipher.decryptor()
decryptedCiphertext = decryptor.update(ciphertext) + decryptor.finalize()
print(decryptedCiphertext)