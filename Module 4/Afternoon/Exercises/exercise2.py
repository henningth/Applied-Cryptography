"""
Exercise 2: Your RSA private key is d=937 and your public key is (n, e)=(2537, 13). Someone sends you the ciphertext c=2222. Decrypt this ciphertext; the resulting plaintext should be a number as well (answer: 18).
"""

n = 2537
e = 13
d = 937

c = 2222

# Decrypt ciphertext
dp = c**d % n

print(dp)