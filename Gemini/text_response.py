from . import GeminiResponseGenerator
from google.genai import types
from pydantic import BaseModel

class GeminiTextGenerator(GeminiResponseGenerator):
    def __init__(self, config:types.GenerateContentConfig):
        super().__init__(model_name="gemini-2.5-flash", config=config)

    def generate_text_single(self, prompt:str) -> str:
        response = self.generate(prompt)
        return response.candidates[0].content.text

