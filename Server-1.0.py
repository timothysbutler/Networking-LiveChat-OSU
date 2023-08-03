# Author: Timothy Butler
# Date: 03/19/2023
# Course: CS372 - 400
# Sources:
# https://note.nkmk.me/en/python-dict-get/
# https://realpython.com/python-sockets/#tcp-sockets

import socket


# Set of common messages and their common responses
messages = {"Hi": "Hello",
            "Hello": "Hello",
            "Hey": "Hello",
            "How are you?": "Great! How are you?",
            "Good": "That's great!",
            "Not good": "I am sorry to hear that",
            "What is your name?": "Mr. Server",
            "Bye": "Leaving so soon? You must type /q to quit.",
            "How's the weather?": "Not sure, I haven't been outside in a long time"
            }
help_message = "The server is limited to certain sayings. They must be spelled exactly how they appear." \
               "Here are the following options:\n" + str(list(messages.keys()))

HOST = "localhost"
PORT = 64644
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}!")
    while True:
        data = conn.recv(4096).decode()
        print(data)
        # if /q, then quit
        if data == '/q':
            break
        # If Help, send help message
        elif data == 'Help':
            print(">" + help_message)
            conn.send(help_message.encode())
        # Search through known messages to find match, then send response
        elif data in messages.keys():
            response = messages.get(data)
            print(">" + response)
            conn.send(response.encode())
        # Else, server does not understand
        else:
            print(">Sorry, I do not understand.")
            conn.send(b"Sorry, I do not understand.")
    # Close the connection
    conn.close()
