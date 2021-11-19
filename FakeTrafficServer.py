# Program to receive and respond to regular TCP packets from one node to another
# Written by Ray Loerke

import socket
import time

# Get the server's IP and desired Port from the user
# Formatting example: '127.0.0.1'
destIP = input("Input the IP of the destination node: ")
# Formatting example: 65432
destPort = input("Input the Port you would like to connect on: ")

# Set up the socket with standard parameters and bind it to the given IP and port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((destIP, destPort))

# Listen for incoming connections
s.listen(0)

# Accept connections and store the connecting socket and address for later use
conn, addr = s.accept()

# These are the arbitrary messages that will be sent to the client
mssgList = [b'I hate this new hat!', b'It is a terrible day!', b'Why is the sky so grey?', b'I hate the color purple',
            b'Why do I have so many pencils?', b'This sucks!']

# Continuously send messages from mssgList to the client with a slight delay in-between each
while True:
    for x in mssgList:
        conn.sendall(x)
        time.sleep(1)

