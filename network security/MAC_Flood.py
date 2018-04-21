from scapy.all import *
pkt=Ether(src=RandMAC(),dst=RandMAC())
sendp(pkt,loop=1)