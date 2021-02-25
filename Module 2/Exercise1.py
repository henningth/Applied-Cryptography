"""
Exercise 1: Let plaintext = 0b1100 and key = 0b1001. (Note: in Python, you can define an integer by using e.g. x = 0b1111 (which will create a variable called x with the value 15). Also note that XOR is only defined between two integers.

(a): Compute the XOR of plaintext and key, call this the ciphertext.

(b): Compute the XOR of ciphertext and the key. What do you observe?

(c): Change one bit of the ciphertext, and compute the XOR of it and the key. What happens to the plaintext? (Note: This property is called malleability.)
"""

plaintext = 0b1100
key = 0b1001

# (a): Compute the XOR of plaintext and key, call this the ciphertext.

ciphertext = plaintext ^ key

print(plaintext)
print(key)
print(ciphertext)

print("Ciphertext in binary: ", bin(ciphertext))

# (b): Compute the XOR of ciphertext and the key. What do you observe?

decrypted = ciphertext ^ key

#print(decrypted)
print("Decrypted in binary: ", bin(decrypted))

# (c): Change one bit of the ciphertext, and compute the XOR of it and the key. What happens to the plaintext? (Note: This property is called malleability.)
changedCiphertext = 0b1101

changedResult = changedCiphertext ^ key

#print(changedResult)
print("Decrypted (changed) in binary: ", bin(changedResult))
