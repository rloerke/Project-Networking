# Program to send regular TCP packets to a node
# Written by Ray Loerke

import socket
import time

# Get the server's IP and Port from the user
# Formatting example: '127.0.0.1'
destIP = input("Input the IP of the destination node: ")
# Formatting example: 65432
destPort = input("Input the Port you would like to connect on: ")

# Set up the socket with standard parameters and connect to it with the given IP and port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((destIP, destPort))

# These are the arbitrary messages that will be sent to the server
mssgList = [b'You have a cool hat!', b'What a nice day!', b'What color is the sky?', b'I like the color purple.',
            b'How many pencils do you have?', b'This is fun.']

# Continuously send messages from mssgList to the server with a slight delay in-between each
while True:
    for x in mssgList:
        s.sendall(x)
        time.sleep(1)

