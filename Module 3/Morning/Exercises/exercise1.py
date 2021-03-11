"""
Exercise 1: This exercise is about Python bytearrays.
"""

"""
(a): Begin by defining an empty bytearray, call it barr1. Also, define a bytes-object with contents “Python 3 programming”. Call it barr2.
"""
barr1 = bytearray()
barr2 = b'Python 3 programming'

"""
(b): Copy the contents of barr2 into barr1, except that the “3” should be a “2”. In other words, the resulting bytearray should read: “Python 2 programming” (Hint: Similar to lists, you can slice bytearrays: for example use barr1[0:4] to get the first 4 bytes from barr1.)
"""
barr1 = barr2[0:7] + b'2' + barr2[8:]
# Alternatively, use replace function
barr1 = barr2.replace(b'3', b'2')

"""
(c): Compute the number of bytes in barr1 and barr2. (Hint: this is similar to computing the number of elements in a list)
"""
print(len(barr1))
print(len(barr2))

"""
(d): What is the value and type of the fifth byte in barr1?
"""
print(barr1[4])
print(type(barr1[4]))

"""
(e): Use a Python-builtin function to find the ASCII character of the fifth byte in barr1?
"""
print(chr(barr1[4]))

"""
(f): Use a Python-builtin function to print the hexadecimal representation of the bytearray barr1.
"""
print(barr1.hex())