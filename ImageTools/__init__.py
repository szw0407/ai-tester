#!/usr/bin/env python3
"""
Send an image to a local OllamaClient vision model using the Python client and PIL (Pillow).

Prereqs:
- OllamaClient installed and running: https://ollama.com
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

import PIL
from PIL.Image import Image
import ollama
import httpx
import re
import ftplib
def load_image(path:str) ->Image:
    if path.startswith("http"):
        img = httpx.get(path)
        img = PIL.Image.open(io.BytesIO(img.content))
    elif path.startswith("ftp"):
        parsed = httpx.URL(path)
        ftp = ftplib.FTP(parsed.host)
        ftp.login()
        r = io.BytesIO()
        ftp.retrbinary(f"RETR {parsed.path}", r.write)
        r.seek(0)
        img = PIL.Image.open(io.BytesIO(r.read()))
        ftp.quit()
    else:
        # we think this is just a local file path
        img = PIL.Image.open(path)
    return img



def encode_image_to_base64(img: Image,
                            max_size: Optional[int] = None) -> str:
    """
    Load an image with PIL, optionally downscale, and return a Base64-encoded PNG string.
    Some models perform faster with reasonably sized inputs.
    """


    # Convert to RGB to avoid issues with modes like RGBA, P, etc.
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")

    # Optionally downscale the image to a maximum dimension (keeps aspect ratio)
    if max_size:
        img.thumbnail((max_size, max_size), Image.LANCZOS)

    buf = io.BytesIO()
    # Save to PNG in-memory for consistent encoding
    img.save(buf, format="jpeg")
    img.save("temp.png", format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return b64
