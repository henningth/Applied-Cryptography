"""
Server script for the client-server chat program
"""

import socket

host = '127.0.0.1'  # The server's hostname or IP address
port = 12345        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by:", addr)
        while True:
            r_data = conn.recv(1024)
            if not r_data:
                break
            print("Data received: ", r_data)
            s_data = input("Enter data to send: ")
            conn.sendall(s_data.encode())
