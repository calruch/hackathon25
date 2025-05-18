#!/bin/bash

# Find the port associated with the current time
curtime=$(date +"%M")

offcur=$(($curtime + 1))
offcur1=$(($curtime ))
#offcur2=$(($curtime))

# text file port hopping scheme
#nodePort=$(cat randNodePort.txt | awk -v line="$curtime" 'NR == line')
#nodePort2=$(cat randNodePort.txt | awk -v line="$offcur" 'NR == line')
#nodePort3=$(cat randNodePort.txt | awk -v line="$offcur2" 'NR == line')

nodePort1=$((($offcur * 46) + 30000))
nodePort2=$((($offcur1 * 46) + 30000))
#nodePort3=$((($offcur2 * 46) + 30000))

# This will patch the service nodePort
microk8s kubectl patch svc nodeport-svc --type merge -p "{\"spec\":{\"ports\": [{\"port\":80,\"targetPort\": 5000,\"nodePort\": $nodePort1}]}}"
microk8s kubectl patch svc honeyport-svc --type merge -p "{\"spec\": {\"ports\": [{\"name\": \"http\", \"port\": 80,\"targetPort\": 80,\"nodePort\": $nodePort2}]}}"


# This will return the new nodePort to the calling process
echo "Main services are hosted on: " $nodePort1
echo "Honeypot http services are hosted on: " $nodePort2
