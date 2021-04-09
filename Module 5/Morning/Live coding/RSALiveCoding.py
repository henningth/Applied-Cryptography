"""
Use the Cryptography module in Python to encrypt and decrypt data using RSA

Use the private and public keys that we generated in the previous slides (the two PEM files)

Check that the encryption is correct

Use OAEP padding (PKCS1.5 is only for legacy)
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

# Encrypt some data using public key
plaintext = b'Hello World'
ciphertext = public_key.encrypt(plaintext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))

print(ciphertext.hex())

# Decrypt the ciphertext
decryptedtext = private_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))

print(decryptedtext)