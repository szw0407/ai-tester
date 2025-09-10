#!/usr/bin/env python3
"""
Send an image to a local Ollama vision model using the Python client and PIL (Pillow).

Prereqs:
- Ollama installed and running: https://ollama.com
- A vision-capable model pulled (e.g., llava or llama3.2-vision):
    ollama pull llava
    # or
    ollama pull llama3.2-vision

- Python deps:
    pip install -r requirements.txt

Usage:
    python analyze_image.py /path/to/image.jpg --prompt "Describe this image" --model llava
    python analyze_image.py /path/to/image.png --prompt "What text is visible?" --model llama3.2-vision --stream
"""

import base64
import io
import os
import sys
from typing import Optional

from PIL import Image
import ollama


def encode_image_to_base64(image_path: str, max_size: Optional[int] = None) -> str:
    """
    Load an image with PIL, optionally downscale, and return a Base64-encoded PNG string.
    Some models perform faster with reasonably sized inputs.
    """
    img = Image.open(image_path)

    # Convert to RGB to avoid issues with modes like RGBA, P, etc.
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")

    # Optionally downscale the image to a maximum dimension (keeps aspect ratio)
    if max_size:
        img.thumbnail((max_size, max_size), Image.LANCZOS)

    buf = io.BytesIO()
    # Save to PNG in-memory for consistent encoding
    img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return b64
