"""
Exercise 1: Consider the following Python code for simple random number generation:

import random, time
current = time.time()
random.seed(current)
r1 = random.randrange(0, 65534)
random.seed(current)
r2 = random.randrange(0, 65534)
print(r1)
print(r2)

Does this code produce consecutive random numbers? If not, suggest an improvement.
"""

import random, time
current = time.time()
random.seed(current)
r1 = random.randrange(0, 65534)
#random.seed(current)
r2 = random.randrange(0, 65534)
print(r1)
print(r2)