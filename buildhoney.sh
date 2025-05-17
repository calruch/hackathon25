#! /bin/bash

if [ $# -eq 0 ]; then
    cd opencanary
    docker build -t canaryhoney -f Dockerfile.latest .
    cd ..
    docker tag canaryhoney:latest localhost:32000/canaryhoney:k8s
    docker push localhost:32000/canaryhoney:k8s
    microk8s kubectl apply -f honeydeploy.yaml
else
    microk8s kubectl apply -f honeydeploy.yaml
fi



