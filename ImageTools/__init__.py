
"""
Some tools used to process images.
"""

import base64
import io

from typing import Optional

import PIL
from PIL.Image import Image

import httpx
import re
import ftplib
def load_image(path:str, max_size:Optional[tuple[int, int]] = None) ->Image:
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
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")

    # Optionally downscale the image to a maximum dimension
    if max_size is not None:
        img = img.resize(max_size)
    return img



def encode_image_to_base64(img: Image| str,
                            max_size: Optional[tuple[int, int]] = None) -> str:
    """
    Load an image with PIL, optionally downscale, and return a Base64-encoded PNG string.
    Some models perform faster with reasonably sized inputs.
    """
    if isinstance(img, str):
        img = load_image(img)
    # Convert to RGB to avoid issues with modes like RGBA, P, etc.
    buf = io.BytesIO()
    # convert to JPEG, to make openai happy.
    img.save(buf, format="jpeg")
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return b64
