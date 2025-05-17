#!/bin/bash

curtime=$(date +"%M")
if [ $curtime -eq 0 ]; then
    curtime++ 
fi
newPort=$(cat randport.txt | awk -v line="$curtime" 'NR == line')
newNodePort=$(cat randNodePort.txt | awk -v line="$curtime" 'NR == line')

nodeIP=$(microk8s kubectl get svc nodeport-svc | awk '{print $3}' | head -n 2 | tail -n 1)


if [ $# -eq 0 ]; then
    curl localhost:$newNodePort

elif [ $1 -eq 1 ]; then
    firefox localhost:$newNodePort

elif [ $1 -eq 2 ]; then
    curl $nodeIP:$newPort

elif [ $1 -eq 3 ]; then
    firefox $nodeIP:$newPort

else
    echo "Please enter an option"
    echo "no Arguments - curl through localhost"
    echo "1 - firefox through localhost"
    echo "2 - curl through the nodeIP using the port"
    echo "3 - firefox through the nodeIP using the port"
fi 

