#!/bin/env python3

from scapy.all import *
import sys

def main():
    file = sys.argv[1]
    pcap = rdpcap(file)
    
    pSession = pcap.sessions()
    packetList = [] # list of all of the packets
    for pSession, sessions in pSession.items():        
        for packet in sessions:
            if(packet.haslayer(TCP)):
                packetList.append(packet)
                if(packetNum != None):
                    check = False

def printRaw(list):
    for i in range(0, len(list)):
        if(list[i].haslayer(Raw)):
            print(f"packet {i}:\n {list[i][Raw].load}")

if __name__ == "__main__":
    main()
