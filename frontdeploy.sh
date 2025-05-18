\#!/bin/bash
cd Login_Gateway 
docker build -t gateway:latest .

docker tag gateway:latest localhost:32000/gateway:k8s
docker push localhost:32000/gateway:k8s

microk8s kubectl apply -f gateway-config.yaml
cd ..

