"""
Generate a public and private ECC key
Use curve SECP384R1
Save these keys in separate PEM files
Load the keys from PEM files
"""

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Generate server private key
server_private_key = ec.generate_private_key(ec.SECP384R1())

# Generate server public key
server_public_key = server_private_key.public_key()

# Serialize key
serializated_public_key = server_public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

print(serializated_public_key) # Can be saved in a file or sent over a socket connection

