from scapy.all import *
pkt=Ether(src=RandMAC())/IP(dst='192.168.1.2',src=RandIP('192.168.1.*'))/ICMP()
sendp(pkt,loop=0,count=1000)