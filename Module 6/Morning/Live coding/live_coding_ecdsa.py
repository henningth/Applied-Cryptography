"""
Use ECDSA to sign and verify some data of your own choice
Use the curve SECP384R1 and hash algorithm SHA256
Print the signature in the console
"""

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

private_key = ec.generate_private_key(ec.SECP384R1())

message = b'Message to be signed.'

signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

public_key = private_key.public_key()

print(signature)