"""
Exercise 2: Write a Python program which implements the anonymous Diffie-Hellman key exchange. Use p=23 and g=5 as parameters. For this part, it is sufficient to test the key exchange in the same script
"""

from random import randint

# Parameters
p = 23
g = 5

# Alice generates her private and public number
a = randint(1,20)
A = g**a % p

# Bob generates his private and public number
b = randint(1,20)
B = g**b % p

# Alice computes shared secret
S_Alice = B**a % p

# Bob computes his shared secret
S_Bob = A**b % p

# Check if they are equal
if S_Alice == S_Bob:
    print("They are equal, shared value:" + str(S_Alice))
    if S_Alice == g**(a*b) % p:
        print("Shared secret equals g**(a*b) % p")
else:
    print("They are different.")
    print("S_Alice:" + str(S_Alice))
    print("S_Bob:" + str(S_Bob))