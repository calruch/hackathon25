# backend/Dockerfile
FROM nvidia/cuda:11.7-runtime-ubuntu22.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]