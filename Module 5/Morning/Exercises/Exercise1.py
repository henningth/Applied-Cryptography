"""
Exercise 1: In this exercise, you are to encrypt and decrypt a message using RSA in the Cryptography library. Start by downloading today’s RSA live-coding example from GitHub.

(a): Run the code which generates RSA keys and saves them in separate PEM files. You should now have two PEM files, one for the private key and one for the public key. Use the parameter 65537 as public exponent, and a key size of 2048 when generating the keys.

(b): Encrypt a message of you own choice using RSA, using the code you downloaded. Use the public key for encrypting your message.

(c): Decrypt the message you encrypted in the previous part. Which key do you need to use?

(d): Encrypt the file Dice.png using RSA. Does it work? If not, what is the problem?

(e): Check what is the largest number of bytes you can encrypt using RSA with the specified parameters. (Hint: it is sufficient to test with random plaintexts)

(f): Based on the above, do you think that RSA is suitable for encrypting large files? If not, suggest an alternative approach.
"""

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding # For OAEP padding
from cryptography.hazmat.primitives import hashes

# Generate private key
private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend())

# Generate public key (from the private key)
public_key = private_key.public_key()

# Serialize the private key object
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption())

# Serialize the public key object
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo)

# Save private key to a file
with open("private_key.pem", "wb") as f:
    f.write(pem_private)

# Save public key to a file
with open("public_key.pem", "wb") as f:
    f.write(pem_public)

# Opens the Dice.png file
with open("Dice.png", "rb") as f: # We can't encrypt this file directly, since it's too large
    plaintext = f.read()

# Encrypt some data using public key
#plaintext = b'Hello World'

# Test what is the largest number of bytes we can encrypt using RSA
from os import urandom

for i in range(1,2048):
    try:
        # Generate random plaintext
        plaintext = urandom(i)
        ciphertext = public_key.encrypt(plaintext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    except ValueError as ve:
        print(ve)
        print("Largest number of bytes: " + str(i-1))
        break

#print(ciphertext.hex())

# Decrypt the ciphertext
decryptedtext = private_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))

#print(decryptedtext)