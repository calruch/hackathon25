#!/bin/bash
./takedown.sh
microk8s kubectl delete all --all
microk8s ctr images rm $(microk8s ctr images ls name~='localhost:32000' | awk {'print $1'})
docker image prune 
#sudo microk8s reset
microk8s enable registry
microk8s enable dns

