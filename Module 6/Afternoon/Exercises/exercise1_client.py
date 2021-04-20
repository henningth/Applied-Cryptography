"""
Exercise 1: Chat client using Diffie Hellman key exchange and 
AES-CTR-128 for symmetric encryption.
Client script.
"""
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from os import urandom
import socket

host = '127.0.0.1'  # The server's hostname or IP address
port = 12345        # The port used by the server

def encrypt(plaintext, key, nonce):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

def decrypt(ciphertext, key, nonce):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

client_private_key = ec.generate_private_key(ec.SECP384R1())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    print("Connected to: ", (host, port))
    # Send public key to server
    client_public_key = client_private_key.public_key()
    # Serialize the public key before sending it
    serialized_public_key = client_public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
    # Send the serialized public key to the server
    s.send(serialized_public_key)
    # Receive server's serialized public key
    serialized_server_public_key = s.recv(1024)
    #print(serialized_server_public_key)
    # Deserialize server's public key
    server_public_key = serialization.load_pem_public_key(serialized_server_public_key)
    #print(server_public_key)
    # Get shared key
    client_shared_key = client_private_key.exchange(ec.ECDH(), server_public_key)
    # Derive shared secret
    derived_shared_key = HKDF(hashes.SHA256(), 32, None, b'Server shared key').derive(client_shared_key)
    print(derived_shared_key)
    # Receive nonce
    nonce = s.recv(16)
    while True:
        s_plaintext = input("Enter data to send: ")
        s_ciphertext = encrypt(s_plaintext.encode(), derived_shared_key, nonce)
        s.sendall(s_ciphertext)
        r_ciphertext = s.recv(1024)
        r_plaintext = decrypt(r_ciphertext, derived_shared_key, nonce)
        print('Received', r_plaintext)