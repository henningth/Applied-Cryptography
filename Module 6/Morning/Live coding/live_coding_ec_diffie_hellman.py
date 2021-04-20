"""
Implement Elliptic Curve Diffie-Hellman key exchange in Python using the Cryptography library
Use https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ec/#elliptic-curve-key-exchange-algorithm 
Print the shared secret in the console
Compare with the ”standard” Diffie-Hellman key exchange done in the first live coding.
"""

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# Generate server private key
server_private_key = ec.generate_private_key(ec.SECP384R1())

# Generate client private key
client_private_key = ec.generate_private_key(ec.SECP384R1())

# Generate server public key
server_public_key = server_private_key.public_key()

# Generate client public key
client_public_key = client_private_key.public_key()

# Perform key exchange (server's point of view)
server_shared_key = server_private_key.exchange(ec.ECDH(), client_public_key)

# Perform key derivation (server's point of view)
server_derived_key = HKDF(hashes.SHA256(), 32, None, b'Server derived key').derive(server_shared_key)

# Perform key exchange (client's point of view)
client_shared_key = client_private_key.exchange(ec.ECDH(), server_public_key)

# Perform key derivation (client's point of view)
client_derived_key = HKDF(hashes.SHA256(), 32, None, b'Server derived key').derive(client_shared_key)

print("server_derived_key:", server_derived_key)
print("client_derived_key:", client_derived_key)

if server_derived_key == client_derived_key:
    print("They match.")
else:
    print("They do not match.")