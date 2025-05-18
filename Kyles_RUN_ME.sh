#!/usr/bin/env bash
set -euo pipefail
trap 'echo "SOMETHING FAILED!!! (╯°□°）╯︵ ┻━┻"' ERR
export PATH="$PATH:/snap/bin"



docker build -t frontend:latest frontend
docker build -t weather:latest weather
docker tag frontend:latest localhost:32000/frontend:k8s
docker tag weather:latest localhost:32000/weather:k8s
docker push localhost:32000/frontend:k8s
docker push localhost:32000/weather:k8s

microk8s kubectl apply -f frontend/config-test.yaml
microk8s kubectl apply -f weather/config.yaml
