"""
Exercise 3: Using the private key d=937 and public key (n, e)=(2537, 13), generate two different ciphertexts (you choose which numerical values you want to encrypt). Multiply the two ciphertexts together and decrypt the result of this multiplication. What can you observe in the decrypted plaintext, with respect to the initial plaintexts?
"""

n = 2537
e = 13
d = 937

p1 = 21
p2 = 44

print(p1 * p2)

# Encrypt
c1 = p1**e % n
c2 = p2**e % n

# Decrypt c1*c2
cmult = c1*c2
pmult = cmult**d % n

print(pmult)