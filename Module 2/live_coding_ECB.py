"""
Live coding AES-ECB
"""

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = os.urandom(16)

cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB(), backend=default_backend())

# Encryption
plaintext = b'Yellow SubmarineYellow SubmarineYellow SubmarineYellow Submarine'
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()
print(ciphertext)

# Decryption
decryptor = cipher.decryptor()
decryptedPlaintext = decryptor.update(ciphertext) + decryptor.finalize()
print(decryptedPlaintext)