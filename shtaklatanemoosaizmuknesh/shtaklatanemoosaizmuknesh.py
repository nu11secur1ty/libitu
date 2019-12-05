#!/usr/bin/python
# by V.Varbanovski @nu11secur1ty
from scapy.all import *
from scapy.error import Scapy_Exception

print("Type the interface which you want to sniff")
cap_iface=raw_input()
filter_message="http"
count=0
def pktTCP(pkt):
    global count
    if pkt.haslayer(TCP) and pkt.getlayer(TCP).dport == 80 and pkt.haslayer(Raw):
            count=count+1
            print pkt.getlayer(Raw).load
sniff(iface=cap_iface,prn=pktTCP) 
