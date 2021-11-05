# Program to receive and respond to regular TCP packets from one node to another
# Written by Ray Loerke

import socket
import time

# Formatting example: '127.0.0.1'
destIP = input("Input the IP of the destination node: ")
# Formatting example: 65432
destPort = input("Input the Port you would like to connect on: ")

s = socket.socket(socket.PF_PACKET, socket.SOCK_STREAM)
s.bind((destIP, destPort))

conn, addr = s.accept()

mssgList = [b'I hate this new hat!', b'It is a terrible day!', b'Why is the sky so grey?', b'I hate the color purple',
            b'Why do I have so many pencils?', b'This sucks!']

while True:
    for x in mssgList:
        conn.sendall(x)
        time.sleep(1)

