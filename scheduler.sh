#!/bin/bash

# Set up of the cluster - Originally on port 30080
./buildall.sh

#Set up the Random port list text file (30001-32766)
#./randport.sh

# Hop off of the initial port
newPort=$(./hop.sh | tail -n +2)

#Enter Port Hopping Loop - repeat every 60 seconds
while sleep 10; do
#    newPort=$(./hop.sh | tail -n +2) 
    ./hop.sh
done


