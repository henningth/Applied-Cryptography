"""
Example program which demonstrates the effect 
of passing arguments to a Python script using the argparse module.
"""

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

# Compute hash of file (reuse code from Module 3)

# Compare hash to the value provided by the user, print either OK or FAIL