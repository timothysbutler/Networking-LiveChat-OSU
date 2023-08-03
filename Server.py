# Author: Timothy Butler
# Date: 03/19/2023
# Course: CS372 - 400
# Sources:
# https://realpython.com/python-sockets/#tcp-sockets

import socket

HOST = "localhost"
PORT = 64644
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on: {HOST} on Port: {PORT}...")
    conn, addr = s.accept()
    print(f"Connected by {addr}!\nWait for message, then respond...")
    while True:
        data = conn.recv(4096).decode()
        print(data)
        # if /q, then quit
        if data == '/q':
            break
        message = input('>')
        conn.send(message.encode())
        # if /q, then quit
        if message == '/q':
            break
    # Close the connection
    conn.close()

