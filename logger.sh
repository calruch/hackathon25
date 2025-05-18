#!/bin/bash

#osqueryi --json '' > file.json
mkdir -p captures
cd captures

while sleep 2; do
    sudo tcpdump -G 60 -i enp0s3 icmp or tcp -w 'dump_%Y-%m-%d_%H:%M:%S.pcap'
done

