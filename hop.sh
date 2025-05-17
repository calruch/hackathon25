#!/bin/bash

# Find the port associated with the current time
curtime=$(date +"%M")
if [ $curtime -eq 0 ]; then
    curtime++
fi

Port=$(cat randport.txt | awk -v line="$curtime" 'NR == line')
nodePort=$(cat randNodePort.txt | awk -v line="$curtime" 'NR == line')


# This will patch the service nodePort
microk8s kubectl patch svc nodeport-svc --type merge -p "{\"spec\":{\"ports\": [{\"port\":$Port,\"targetPort\": 5000,\"nodePort\": $nodePort}]}}"

# This will return the new nodePort to the calling process
echo $nodePort
echo $Port

