"""
Exercise 1: Chat client using Diffie Hellman key exchange and 
AES-CTR-128 for symmetric encryption.
Server script.
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

server_private_key = ec.generate_private_key(ec.SECP384R1())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by:", addr)
        # Receive public key from client
        serialized_client_public_key = conn.recv(1024)
        # Deserialize the client's public key
        client_public_key = serialization.load_pem_public_key(serialized_client_public_key)
        #print(client_public_key)
        # Send server's public key to client
        server_public_key = server_private_key.public_key()
        # Serialize the key and send it
        serialized_server_public_key = server_public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
        conn.send(serialized_server_public_key)
        # Get shared key
        server_shared_key = server_private_key.exchange(ec.ECDH(), client_public_key)
        # Derive shared secret
        derived_shared_key = HKDF(hashes.SHA256(), 32, None, b'Server shared key').derive(server_shared_key)
        print(derived_shared_key)
        # Server sends nonce to client
        nonce = urandom(16)
        conn.send(nonce)
        while True:
            r_ciphertext = conn.recv(1024)
            if not r_ciphertext:
                break
            r_plaintext = decrypt(r_ciphertext, derived_shared_key, nonce)
            print("Data received: ", r_plaintext)
            s_plaintext = input("Enter data to send: ")
            s_ciphertext = encrypt(s_plaintext.encode(), derived_shared_key, nonce)
            conn.sendall(s_ciphertext)