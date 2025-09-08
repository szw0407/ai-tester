from PIL.ImageFile import ImageFile
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

from . import GeminiResponseGenerator

class GeminiImageGenerator(GeminiResponseGenerator):
    def __init__(self):
        super().__init__(model_name="gemini-2.5-flash-image-preview")

    def generate_image(self, prompt:str) -> ImageFile | None:
        response = self.generate(prompt)
        for p in response.candidates[0].content.parts:
            if p.text:
                print("Text part:", p.text)
            if p.inline_data is not None:
                return Image.open(BytesIO(p.inline_data.data))

        return None


if __name__ == "__main__":
    prompt = "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
    generator = GeminiImageGenerator()
    image = generator.generate_image(prompt)
    if image:
        image.show()
        image.save("generated_image.png")
    else:
        print("No image generated.")