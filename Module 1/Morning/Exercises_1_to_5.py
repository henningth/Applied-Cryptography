"""
Exercises for lecture 1, morning (lecture 1A)

Python exercises (ex. 1 - 5)
"""

"""
For some tips on these exercises, see https://www.devdungeon.com/content/working-binary-data-python (Links til en ekstern webside.) and https://www.dotnetperls.com/bytes-python (Links til en ekstern webside.)

Exercise 1: Write a Python program which takes a string as input, and prints the individual byte values of the string
"""

# string1 = input("Enter string: ")

# # Convert to bytes
# for i in range(len(string1)):
#     print(string1[i], " in byte is", ord(string1[i]))

"""
Exercise 2: Write a Python program which takes a positive integer as input, and prints the binary and hexadecimal representation of this integer.
"""
# positiveInt = int(input("Enter positive int:"))

# positiveIntBinary = bin(positiveInt)
# positiveIntHexadecimal = hex(positiveInt)

# print(positiveInt)
# print(positiveIntBinary)
# print(positiveIntHexadecimal)

# def intBy(n):
#     if n < 0:
#         return print("must be positive integer")
#     else:
#         n1 = bin(n)
#         n2 = hex(n)
#         return n, n1, n2
 
# a, a1, a2 = intBy(12345)
 
# print("Int:",a,"\n"+"Bin:",a1,"\n"+"Hex:",a2)

"""
Exercise 3: Write a Python program which takes a text string as input and saves it as UTF-8 encoded variable. Test if it works when using Danish letters such as æ, ø, å.
"""

#text = input("Enter text string: ")
#textEncoded = text.encode('UTF-8')
#print(textEncoded)

"""
Exercise 4: Repeat the previous exercise but encode the string in ASCII instead of UTF-8. Does it work? Why or why not?
"""
#text = input("Enter text string: ")
#textEncoded = text.encode('ASCII')
#print(textEncoded)

"""
Exercise 5: Write a Python program that opens a PNG file in binary mode and prints the first 8 bytes of the file (its signature). Compare with https://en.wikipedia.org/wiki/Portable_Network_Graphics#File_header
"""

import os

savefilepath = os.path.dirname(__file__) + "\\" + "Dice.png"


with open(savefilepath, "rb") as file:
    content = file.read(8)
print(content)