"""
Write a Python program that implements a simple RSA scheme
Use p=7 and q=11
Add code that computes the modulus n and generates the private key e and public key d (use small numbers for simplicity)
Use the generated private key to encrypt a message
Use the generated public key to decrypt the ciphertext
"""

# Compute GCD:
def gcd(a, b):
    if a == 1 or b == 1:
        return a
    while a != b:
        if a == 0:
            break
        a, b = b % a, a
    return b

# Our two prime numbers
p = 7
q = 11

# Compute modulus
n = p*q

# Find a number e such that e and (p-1)*(q-1) have no common prime factors
m = (p-1)*(q-1)
for e in range(2, n):
    result = gcd(e, m)
    if result == 1:
        break

# Find the inverse of e, call it d, i.e. the public key
for d in range(2, n):
    result = (e * d) % m
    if result == 1:
        break

# Print public and private keys
print("Private key d:", d)
print("Public key (n,e):", n, e)

# Encrypt using public key
p = 3 # Plaintext
print("Plaintext:", p)
c = p**e % n
print("Ciphertext:", c)

# Decrypt using private key
dp = c**d % n
print("Decr. pl.text:", dp)