#! /bin/bash

if [ $# -eq 0 ]; then
    microk8s kubectl create configmap opencanary-config --from-file=.opencanary.conf=./opencanary/data/.opencanary.conf
    cd opencanary
    docker build -t canaryhoney -f Dockerfile.latest .
    cd ..
    docker tag canaryhoney:latest localhost:32000/canaryhoney:k8s
    docker push localhost:32000/canaryhoney:k8s
    microk8s kubectl apply -f honeydeploy.yaml
else
    microk8s kubectl apply -f honeydeploy.yaml
fi



