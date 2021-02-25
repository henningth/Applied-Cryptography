"""
XOR examples in Python.
"""

plaintext = 65
key = 179

ciphertext = plaintext ^ key

print(ciphertext)

decryptedPlaintext = ciphertext ^ key

print(decryptedPlaintext)