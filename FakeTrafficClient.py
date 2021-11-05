# Program to send regular TCP packets from one node to another
# Written by Ray Loerke

import socket
import time

# Formatting example: '127.0.0.1'
destIP = input("Input the IP of the destination node: ")
# Formatting example: 65432
destPort = input("Input the Port you would like to connect on: ")

s = socket.socket(socket.PF_PACKET, socket.SOCK_STREAM)
s.connect((destIP, destPort))

mssgList = [b'You have a cool hat!', b'What a nice day!', b'What color is the sky?', b'I like the color purple.',
            b'How many pencils do you have?', b'This is fun.']

while True:
    for x in mssgList:
        s.sendall(x)
        time.sleep(1)

