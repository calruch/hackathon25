#!/usr/bin/env bash
set -euo pipefail
trap 'echo "SOMETHING FAILED!!! (╯°□°）╯︵ ┻━┻"' ERR
export PATH="$PATH:/snap/bin"

echo "===== UPDATING PACKAGE LIST ====="
apt update -y
echo ""

echo "===== INSTALLING docker.io & snapd ====="
apt install -y docker.io snapd
echo ""

echo "===== STARTING snapd ====="
systemctl enable --now snapd
systemctl enable --now snapd.apparmor
echo ""

echo "===== INSTALLING microk8s & kubectl ====="
snap install microk8s --classic
snap install kubectl --classic
echo ""

echo "===== ADDING YOU TO docker & microk8s GROUPS ====="
usermod -aG docker "$SUDO_USER"
usermod -aG microk8s "$SUDO_USER"
echo ""

echo "===== ENABLING microk8s ADDONS ====="
microk8s enable registry
echo ""

echo "===== INSTALLING VIRUSES, CRYPTOMINER, AND RASOMWARE ====="
echo "<('-'<)"
microk8s status --wait-ready
echo "(>'-')>"
microk8s kubectl wait -n kube-system deploy/coredns --for=condition=Available --timeout=90s || true
microk8s kubectl wait -n container-registry deploy/registry --for=condition=Available --timeout=90s || true
echo "<('O')> \"You're good to go!\" - Kirby"
sleep 3

echo "===== CONFIGURING DOCKER TO TRUST LOCAL REGISTRY... HOPEFULLY ====="
cat <<EOF >/etc/docker/daemon.json
{"insecure-registries":["localhost:32000"]}
EOF
echo ""

echo "===== RESTARTING docker ====="
systemctl daemon-reload
systemctl restart docker
echo ""

echo "===== SETUP COMPLETE! HOPEFULLY EVERYTHING WORKS ¯\_(ツ)_/¯ ====="
echo "Log out and back in to apply group changes."