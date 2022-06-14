## Networking Project
This project is part of the CS 330: Computer Networking Course taught by Professor Mark Liffiton. 

The purpose of this project is to simulate an ARP Spoofing attack on a simulated network.
To conduct this simulation run the FakeTrafficServer.py file on the first target machine, then run the FakeTrafficClient.py on the second target machine.
These programs simulate traffic between the two target machines by sending arbitrary messages back and forth.

Once this arbitrary traffic is being sent run the ARPSpoofing.py file on the attacking machine to initiate the ARP Spoofing attack.
This program will continuously send spoofed ARP packets to the target machines impersonating the other target.
Network traffic will then be intercepted by the attacking machine which can be captured by a network sniffing tool.
Descriptions on the log files captured during this simulation can be found below.

## Author
Ray Loerke

## Sources
Various code was adapted from:
* https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_arp_spoofing.htm
* https://realpython.com/python-sockets/

## Extra
The Server.py and Client.py files are for reference only. They will not be used in the project. 

## Logs
Sniflog 1, 2 and 3 are the traces captured during the Ettercap MITM attack. 
Log3, 4 and 5 are tshark captures at various points in the project.
-log.txt files are console logs of all three hosts involved during an execution of the attack.