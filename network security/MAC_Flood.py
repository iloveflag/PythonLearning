from scapy.all import *
pkt=Ether(src=RandMAC(),dst=RandMAC())z
sendp(pkt,loop=1)