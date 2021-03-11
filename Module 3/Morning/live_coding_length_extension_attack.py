"""
Length extension attack of the MD5 hash function
"""
from pymd5 import md5, padding

# The original message
m = "Yellow submarine"
h = md5()
h.update(m)
md5digest = h.hexdigest()
print("MD5(", m, "):", md5digest)

# Do the length extension attack
msgLen = len(m)
bits = (msgLen + len(padding(msgLen*8)))*8
# We initialize the md5 object with the *updated* state
hLenatt = md5(state=bytes.fromhex(md5digest), count=bits)
t = " diving"
hLenatt.update(t)
md5digestLenatt = hLenatt.hexdigest()
print("MD5(", m + t, "):", md5digestLenatt)

# Check if this is the same as the MD5 hash of the string "Yellow Submarine Diving"
# computed in one go. Note that we must add padding here also.

m2 = m.encode() + padding(msgLen*8) + t.encode()
#m2 = m.encode() + t.encode() + padding(msgLen*8)
h2 = md5()
h2.update(m2)
md5digestCompleteMsg = h2.hexdigest()
print("MD5(", m2, "):", md5digestCompleteMsg)