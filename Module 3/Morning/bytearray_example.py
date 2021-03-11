"""
Bytearray example
"""

barr = bytearray()
print(len(barr))

barr.append(44)
print(len(barr))
print(barr[0])

barr[0] = 254
print(barr[0])

barr2 = b'Hello world'

barr3 = bytearray()
barr3 = barr2[0:5]
print(barr3)