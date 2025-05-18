#!/usr/bin/env bash

echo "===== BUILDING DOCKER IMAGES ====="
docker build -t gateway:latest Login_Gateway
#docker build -t to-upper:latest Services/ToUpper
docker build -t weather:latest Services/Weather
echo ""

echo "===== TAGGING IMAGES ====="
docker tag gateway:latest localhost:32000/gateway:k8s
#docker tag to-upper:latest localhost:32000/to-upper:k8s
docker tag weather:latest localhost:32000/weather:k8s
echo ""

echo "===== PUSHING IMAGES ====="
docker push localhost:32000/gateway:k8s
#docker push localhost:32000/to-upper:k8s
docker push localhost:32000/weather:k8s
echo ""

echo "===== DEPLOYING ====="
microk8s kubectl apply -f Login_Gateway/gateway-config.yaml
#microk8s kubectl apply -f Services/ToUpper/config.yaml
#microk8s kubectl apply -f Services/Weather/config.yaml
echo ""
