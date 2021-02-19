"""

General case of Padding Oracle attack on AES-CBC

"""

import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

plaintext = b'Commodore Computer Programming is very interesting and also fun, but can be hard.'

#plaintext = b'Bandit is a tool designed to find common security issues in Python code. To do this, Bandit processes each file, builds an AST from it, and runs appropriate plugins against the AST nodes. Once Bandit has finished scanning all the files, it generates a report.'

blocksize = 16

iv = os.urandom(blocksize)
key = os.urandom(blocksize)

print("Plaintext\t\t\t\t: ", plaintext.decode())

padder = padding.PKCS7(blocksize*8).padder()

paddedPlaintext = padder.update(plaintext) + padder.finalize()

#print("Padded plaintext\t\t\t: ", paddedPlaintext.decode())

cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CBC(iv), backend=default_backend())

encryptor = cipher.encryptor()

ciphertext = encryptor.update(paddedPlaintext) + encryptor.finalize()

#print("Ciphertext: ", ciphertext)

def paddingOracle(ciphertext):
    """
    Takes ciphertext as input, decrypt it and return:
    True if padding is valid
    False otherwise
    """
    decryptor = cipher.decryptor()
    paddedDecryptedPlaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(blocksize*8).unpadder()
    try:
        unpadder.update(paddedDecryptedPlaintext) + unpadder.finalize()
        return True
    except:
        return False

def paddingOracleAttackLastblock(ciphertext):

    randomCiphertext = os.urandom(32)

    intermediateArray = bytearray(16)

    plaintextGuessArray = bytearray(16)

    i = 1

    for byte in range(0,16):

        previousIntermediatesSlice = intermediateArray[17-i:16]

        previousIntermediates = bytearray(len(previousIntermediatesSlice))

        for k in range(1,len(previousIntermediatesSlice)+1):

            previousbyte = previousIntermediatesSlice[-k]

            previousIntermediates[-k] = (byte+1) ^ previousbyte

        for changedByte in range(256):

            changedCiphertextblock = ( changedByte ).to_bytes(1,'little')

            modifiedCiphertext = randomCiphertext[:16-i] + changedCiphertextblock + previousIntermediates + ciphertext[16:]

            modifiedResult = paddingOracle(modifiedCiphertext)

            if modifiedResult:

                # Compute intermediate value
                intermediate = changedByte ^ (byte+1)
                plaintextGuess = ciphertext[15-i+1] ^ intermediate

                intermediateArray[-i] = intermediate

                plaintextGuessArray[-i] = plaintextGuess


        i += 1

    return plaintextGuessArray

numBlocks = len(paddedPlaintext) // 16

plaintextGuess = bytearray((numBlocks-1)*blocksize)

for blockIndex in range(numBlocks,1,-1):

    plaintextGuess[(blockIndex-2)*blocksize:(blockIndex-1)*blocksize] = paddingOracleAttackLastblock(ciphertext[(blockIndex-2)*blocksize:blockIndex*blocksize])

print("Decrypted (without key) plaintext\t: ", plaintextGuess.decode())