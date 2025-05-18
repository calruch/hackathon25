# FOR TESTING
# backend/Dockerfile (CPU-only)

FROM python:3.13-slim
# Install system deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      libgl1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your models (or mount as volume at runtime)
COPY models/ /models/

# Copy service code
COPY app.py config.py ./

# Force CPU and float32 for safety on non-GPU hosts
ENV MODEL_PATH="/models/realisticVisionV60B1_v51HyperInpaintVAE"
ENV LORA_PATH="/models/lora/hqcat"
ENV TORCH_DTYPE="float32"
ENV SECRET_KEY="Gandolf_the_White"

EXPOSE 5000

CMD ["python", "app.py"]

# backend/Dockerfile
# FROM nvidia/cuda:11.7-runtime-ubuntu22.04

# RUN apt-get update && \
#     apt-get install -y python3 python3-pip && \
#     rm -rf /var/lib/apt/lists/*

# WORKDIR /app
# COPY . .
# RUN pip3 install --no-cache-dir -r requirements.txt

# CMD ["python3", "app.py"]