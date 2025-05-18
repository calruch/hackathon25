#! /bin/bash

if [ $# -eq 0 ]; then
    docker build . -t backside
    docker tag backside:latest localhost:32000/backside:k8s
    docker push localhost:32000/backside:k8s
    microk8s kubectl apply -f deploy.yaml
else
    microk8s kubectl apply -f deploy.yaml
fi

