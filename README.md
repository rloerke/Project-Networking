## Networking Project
This project is part of the CS 330: Computer Networking Course taught by Professor Mark Liffiton. 

## Author
The author is Ray Loerke

## Sources
Various code was adapted from:
* https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_arp_spoofing.htm
* https://realpython.com/python-sockets/

## Extra
The Server.py and Client.py files are for reference only. They will not be used in the project. 

FakeTraffic Client and Server will send arbitrary messages to each other. The ARPSpoofing file should perform the actual attack.
The hope is that I will know if the attack is working if I capture packets containing the messages written in the FakeTraffic files.

## Logs
Sniflog 1,2, and 3 are the traces captured during the Ettercap MITM attack. 
Log3,4,5 are tshark captures at various points in the project.
-log.txt files are console logs of all three hosts involved during an execution of the attack.