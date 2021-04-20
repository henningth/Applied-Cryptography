"""
Exercise 2: Download the live coding examples with the Diffie-Hellman key exchange (both classical and elliptic curve versions) from the course Github page. Note: For the classical Diffie-Hellman, use generator=2 and key_size=1024 as parameters, for the elliptic curve Diffie-Hellman, use curve SECP384R1.	
(a): Modify both scripts so that the shared value is printed in the console in hexadecimal format. Compare the two in terms of length.
(b): Compute the time it takes for each of the two scripts to generate a private key. To do this, you can use the time() function from the time module
(c): Compute the time it takes for each of the two scripts to derive a shared key. To do this, you can use the time() function from the time module
"""

from time import time

"""
Classical Diffie-Hellman
"""
print("===================================================")
print("   Classical Diffie Hellman   ")
print("===================================================")
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# Generate parameters for D.H. key exchange
start = time()
parameters = dh.generate_parameters(generator=2, key_size=1024) # g and key size
end = time()
print("generate_parameters: ", end - start)

# Generate Alice's private key and corresponding public key
start = time()
private_key_alice = parameters.generate_private_key() # a
end = time()
print("generate_private_key (Alice): ", end - start)

public_key_alice = private_key_alice.public_key() # A

# Generate Bob's private key and corresponding public key
start = time()
private_key_bob = parameters.generate_private_key() # b
end = time()
print("generate_private_key (Bob): ", end - start)

public_key_bob = private_key_bob.public_key() # B

# Generate shared key (Alice's point of view)
shared_key_alice = private_key_alice.exchange(public_key_bob) # B**a

# Derive key for use in subsequent communication
start = time()
derived_key_alice = HKDF(hashes.SHA256(), 32, None, b'Derived key Alice').derive(shared_key_alice)
end = time()
print("derive shared key (Alice): ", end - start)

# Generate shared key (Bob's point of view)
shared_key_bob = private_key_bob.exchange(public_key_alice) # A**b

# Derive key for use in subsequent communication
start = time()
derived_key_bob = HKDF(hashes.SHA256(), 32, None, b'Derived key Bob').derive(shared_key_bob)
end = time()
print("derive shared key (Bob): ", end - start)

#print("derived_key_alice", derived_key_alice.hex())
#print("derived_key_bob", derived_key_bob.hex())

"""
Elliptic Curve Diffie Hellman
"""
print("===================================================")
print("   Elliptic Curve Diffie Hellman   ")
print("===================================================")
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# Generate server private key
start = time()
server_private_key = ec.generate_private_key(ec.SECP384R1())
end = time()
print("generate_private_key (Server): ", end - start)

# Generate client private key
start = time()
client_private_key = ec.generate_private_key(ec.SECP384R1())
end = time()
print("generate_private_key (Client): ", end - start)

# Generate server public key
server_public_key = server_private_key.public_key()

# Generate client public key
client_public_key = client_private_key.public_key()

# Perform key exchange (server's point of view)
server_shared_key = server_private_key.exchange(ec.ECDH(), client_public_key)

# Perform key derivation (server's point of view)
start = time()
server_derived_key = HKDF(hashes.SHA256(), 32, None, b'Server derived key').derive(server_shared_key)
end = time()
print("derive shared key (Server): ", end - start)

# Perform key exchange (client's point of view)
client_shared_key = client_private_key.exchange(ec.ECDH(), server_public_key)

# Perform key derivation (client's point of view)
start = time()
client_derived_key = HKDF(hashes.SHA256(), 32, None, b'Server derived key').derive(client_shared_key)
end = time()
print("derive shared key (Client): ", end - start)

#print("server_derived_key:", server_derived_key.hex())
#print("client_derived_key:", client_derived_key.hex())