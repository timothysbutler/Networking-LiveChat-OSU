# Author: Timothy Butler
# Date: 03/19/2023
# Course: CS372 - 400
# Sources:
# https://realpython.com/python-sockets/#tcp-sockets

import socket
import time

# Connect to the server
HOST = "localhost"
PORT = 64644
print(f"Connecting to {HOST} on Port {PORT}...")
time.sleep(0.5)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected!\nLet's start chatting!")
    time.sleep(0.5)
    print("Enter a message...")
    while True:
        message = input('>')
        s.send(message.encode())
        # if /q, then quit
        if message == '/q':
            break
        data = s.recv(4096).decode()
        # if /q, then quit
        if data == '/q':
            break
        print(data)
