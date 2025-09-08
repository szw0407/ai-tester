import os
from google import genai
from google.genai import types


class GeminiResponseGenerator:
    client = genai.Client(
    api_key=os.getenv("GENAI_API_KEY")
)
    config:types.GenerateContentConfig = None
    model_name:str
    def __init__(self, model_name:str, config:types.GenerateContentConfig=None):
        self.model_name = model_name
        self.config = config if config else self.config

    def generate(self, prompt:str) -> types.GenerateContentResponse:
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[prompt],
            config=self.config
        )
        return response