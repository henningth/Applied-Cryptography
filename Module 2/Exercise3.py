"""
Exercise 3: Starting from the AES-ECB live coding example, add functions so that the user can input an arbitrary text string. This text string should then be encrypted, and the ciphertext should be printed in the console. Be sure to check that your code can decrypt the ciphertext also.
"""

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

key = os.urandom(16)

cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB(), backend=default_backend())

plaintext = input("Enter plaintext: ").encode()

# Add padding and then encrypt
#plaintext = b'Yellow Submarin'
padder = padding.PKCS7(128).padder()
encryptor = cipher.encryptor()
paddedPlaintext = padder.update(plaintext) + padder.finalize()
ciphertext = encryptor.update(paddedPlaintext) + encryptor.finalize()
print(ciphertext)

# Decrypt and then remove padding
decryptor = cipher.decryptor()
unpadder = padding.PKCS7(128).unpadder()
decryptedPlaintext = decryptor.update(ciphertext) + decryptor.finalize()
unpaddedDecryptedPlaintext = unpadder.update(decryptedPlaintext) + unpadder.finalize()
print(unpaddedDecryptedPlaintext)