"""
Exercise 1: Download the live coding example of the ECDSA signature and verification from the course Github page.
(a): Try to sign some data of your own choice. Print the signatures.
(b): Verify the signed data from the previous part. Have the program print whether the verification failed or succeeded.
(c): Change one byte in the data to be verified and try to verify it. What happens?
"""

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

private_key = ec.generate_private_key(ec.SECP384R1())

message = b'Message to be signed!'

signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

new_signature = b'\x04' + signature[1:] # change the first byte

# Use public key for verification
public_key = private_key.public_key()
try:
    public_key.verify(new_signature, message, ec.ECDSA(hashes.SHA256()))
    print("Verification OK")
except InvalidSignature:
    print("Verification FAIL")

print(signature)