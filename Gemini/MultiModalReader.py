from google.genai.types import GenerateContentResponse

from . import GeminiResponseGenerator
from google.genai import types
from PIL.Image import Image
from ImageTools import encode_image_to_base64, load_image
from httpx import URL
import httpx
class GeminiMultiModalQA(GeminiResponseGenerator):
    def __init__(self, model_name: str = "gemini-2.5-pro"):
        super().__init__(model_name=model_name)

    def generate_with_image(self, prompt:str, image:Image|URL, config:types.GenerateContentConfig = None) -> str:
        image_jpeg_file:bytes = image.tobytes(
            encoder_name="jpeg",
        ) if isinstance(image, Image) else httpx.get(image).content

        response:GenerateContentResponse = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Part.from_bytes(
                    data=image_jpeg_file,
                    mime_type="image/jpeg",
                ),
                prompt,
            ],
            config=config,
        )
        return response.text