# backend/app.py
from io import BytesIO
import os
import base64
from PIL import Image
from flask import Flask, request, jsonify
from diffusers import StableDiffusionInpaintPipeline
import torch

# load config
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize pipeline once
device = "cuda" if torch.cuda.is_available() else "cpu"
pipeline = StableDiffusionInpaintPipeline.from_pretrained(
    Config.MODEL_PATH,
    torch_dtype=getattr(torch, Config.TORCH_DTYPE)
)
# load LoRA
if Config.LORA_PATH:
    pipeline.load_lora_weights(Config.LORA_PATH)
# optimize
pipeline.to(device)
pipeline.enable_attention_slicing()

@app.route("/add-cat", methods=["POST"])
def inpaint():
    # accept multipart/form-data or JSON
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    image_file = request.files['image']
    image = Image.open(image_file).convert("RGB")

    # mask can be base64 from form or file
    mask_data = request.form.get('mask')
    if mask_data and mask_data.startswith('data:image'):
        header, b64 = mask_data.split(',', 1)
        mask = Image.open(BytesIO(base64.b64decode(b64))).convert("RGB")
    elif 'mask' in request.files:
        mask = Image.open(request.files['mask']).convert("RGB")
    else:
        return jsonify({"error": "No mask provided"}), 400

    prompt = request.form.get('description', '')
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # run inpainting
    result = pipeline(
        prompt=prompt,
        image=image,
        mask_image=mask,
        guidance_scale=7.5,
        num_inference_steps=50
    )
    output = result.images[0]

    # encode to base64
    buf = BytesIO()
    output.save(buf, format='PNG')
    b64_out = base64.b64encode(buf.getvalue()).decode('utf-8')

    return jsonify({
        "image": f"data:image/png;base64,{b64_out}"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)