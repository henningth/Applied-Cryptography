"""
Exercise 4: Modify the code from the previous exercise so that the user can choose whether to provide a key or have the program generate a key. Try to encrypt with simple keys such as the all-zeros bitstring.
"""

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


choice = input("Press (R) to generate random key, (E) to enter one ")
if choice == "R":
    key = os.urandom(16)
elif choice == "E":
    while True:
        key = input("Enter key (16 chars.): ").encode()
        if len(key) == 16:
            break

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