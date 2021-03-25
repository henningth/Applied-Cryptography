"""
Exercise 1: Write a Python program that takes a file, a hash-function and a digest as arguments, compares the hash of the file with the digest and prints either OK (if the validation succeeds) or FAIL (if the validation fails). This program should be run from the command-line, so if we have a file dice.png and its SHA1 hash, we should be able to run:

python3 exercise1.py -f dice.png -d 8fa35328213d3ec07ec3e7e5ec930cb95b7fbfe9 -a sha1

and have the program compute the SHA1 hash of the dice.png file and print OK if the computed SHA1 hash matches the argument 8fa35328213d3ec07ec3e7e5ec930cb95b7fbfe9.

To have Python read command-line arguments, you can use the argparse module, an example of this module and its usage is on Github (argumentParserExample.py)

Have the program support the following hash functions: MD5 and SHA1. (You can add other hash functions if you want.)

To test the program, download the file dice.png from the course Github site, and compare with the MD5 and SHA1 hash of this file. The MD5 hash is 3942b3b4bed2e098ea28a0a81fd38e91 and the SHA1 hash is 8fa35328213d3ec07ec3e7e5ec930cb95b7fbfe9.
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Compute specified hash of a file, compare with given digest')

# Add arguments to parser
parser.add_argument('-f', '--file', action='store', dest='file', help='name of file to compute digest of', required=True)
parser.add_argument('-a', '--algorithm', action='store', dest='algorithm', help='hash algorithm', required=True)
parser.add_argument('-d', '--digest', action='store', dest='digest', help='digest to compare to', required=True)

# Parse arguments
args = parser.parse_args()

print("Chosen file: ", args.file)
print("Chosen algorithm: ", args.algorithm)
print("Digest to compare to: ", args.digest)

"""
Fill in the code for the steps required
"""

# Open the file (remember to open the file in binary mode)
with open(args.file, "rb") as f:
    data = f.read()

# Compute hash of file (reuse code from Module 3)
# Use either MD5 or SHA1, based on user's command
if args.algorithm.lower() == "md5":
    h = hashes.Hash(hashes.MD5(), default_backend())
    h.update(data)
    digest = h.finalize().hex()
elif args.algorithm.lower() == "sha1":
    h = hashes.Hash(hashes.SHA1(), default_backend())
    h.update(data)
    digest = h.finalize().hex()
else:
    print("Invalid choice of hash algorithm, choose either MD5 or SHA1.")

# Compare hash to the value provided by the user, print either OK or FAIL
if args.digest == digest:
    print("OK")
else:
    print("FAIL")