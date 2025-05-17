# backend/config.py
import os

class Config:
    # local model paths
    MODEL_PATH = os.getenv("MODEL_PATH", "/models/realisticVisionV60B1_v51HyperInpaintVAE")
    # a LoRA adapter for better feline detail
    LORA_PATH   = os.getenv("LORA_PATH", "/models/lora/hqcat")

    # torch dtype for performance (float16 recommended if GPU supports)
    TORCH_DTYPE = os.getenv("TORCH_DTYPE", "float16")

    # Flask secret
    SECRET_KEY  = os.getenv("SECRET_KEY", "Gandolf_The_White")