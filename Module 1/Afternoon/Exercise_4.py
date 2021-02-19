"""
Exercise 4: Implement a naive random number generator for generating numbers in the range 0 to 191, as follows: Start by generating a random 8-bit value, and interpreting it as an integer. Then reduce this integer modulo 192. Generate a large number of integers in this way and check the probability distribution of the resulting numbers.
"""
import random

numbers = {}

for i in range(10000):

    number = int.from_bytes(random.randbytes(1), "big") % 192

    if (number in numbers):
        numbers[number] += 1

    else:
        numbers[number] = 1

sorted = dict(sorted(numbers.items(), key=lambda item: item[1], reverse=True))

for number in sorted:

    print(number, '\t', sorted[number])