"""
Exercise 5: Consider the following key and nonce, here in their Base64 representation:

Key: WXvqxbAEEM08snXbYgu8bg==

Nonce: ZmRqZW1ma3Jtc2thbXNuZA==

Decrypt the following ciphertext (here in Base64) using AES in CTR mode:

M8owlYB5ewJJ2YFcdLdXJu0DHlv4+9iqUpdpJeRyH3SRqg==

(Hint: to convert from Base64 to bytearray, have a look at the Base64 module in Python)
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import base64

key = "WXvqxbAEEM08snXbYgu8bg=="
nonce = "ZmRqZW1ma3Jtc2thbXNuZA=="
ciphertext = "M8owlYB5ewJJ2YFcdLdXJu0DHlv4+9iqUpdpJeRyH3SRqg=="

keyBytes = base64.b64decode(key)
nonceBytes = base64.b64decode(nonce)
ciphertextBytes = base64.b64decode(ciphertext)

print("Ciphertext blocks ", str(len(ciphertextBytes)/16))

cipher = Cipher(algorithms.AES(keyBytes), modes.CTR(nonceBytes), backend=default_backend())

decryptor = cipher.decryptor()
decryptedCiphertext = decryptor.update(ciphertextBytes) + decryptor.finalize()

print(decryptedCiphertext)