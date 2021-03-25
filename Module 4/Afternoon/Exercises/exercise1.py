"""
Exercise 1: Starting with the live coding from today, experiment with the following, be sure to try several different plaintexts.

(a): Use some other prime numbers than the one in the live coding

(b): Use the same prime number, that is, p = q

(c): Use composite numbers instead of prime numbers

(d): Try to encrypt a plaintext which is larger than the modulus. Does it work?
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
p = 81 # Plaintext
print("Plaintext:", p)
c = p**e % n
print("Ciphertext:", c)

# Decrypt using private key
dp = c**d % n
print("Decr. pl.text:", dp)