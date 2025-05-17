#!/bin/bash

checkPort() {
    cPort=$(cat randport.txt | grep $1 | wc -l)
    echo $cPort
}

checkNodePort() {
    cPort=$(cat randNodePort.txt | grep $1 | wc -l)
    echo $cPort
}

touch randport.txt
echo "" > randport.txt

touch randNodePort.txt
echo "" > randNodePort.txt

for i in {1..61}
do
    Portc=10
    Portc1=10
    while [ "$Portc1" -ne 0 ]; do
        newPort1=$(($RANDOM % (1000 - 20 + 1) + 20))
        Portc1=$(checkPort $newPort1)
    done
    while [ "$Portc" -ne 0 ]; do
        newPort=$(($RANDOM % (32766 - 30001 + 1) + 30001))
        Portc=$(checkNodePort $newPort)
    done
    echo $newPort1 >> randport.txt
    echo $newPort >> randNodePort.txt
done
