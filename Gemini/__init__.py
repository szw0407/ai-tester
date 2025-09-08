import os
from google import genai
from google.genai import types
from pydantic import BaseModel


class GeminiResponseGenerator:
    client = genai.Client(
    api_key=os.getenv("GENAI_API_KEY")
)
    model_name:str
    def __init__(self, model_name:str):
        self.model_name = model_name

    def generate(self, prompt:str, config:types.GenerateContentConfig | types.GenerateImagesConfig | types.GenerateVideosConfig | None = None) -> types.GenerateContentResponse | types.GenerateImagesResponse | types.GenerateVideosResponse:
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[prompt],
            config=config
        )
        return response