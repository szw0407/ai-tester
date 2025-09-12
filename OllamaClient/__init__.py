from typing import Literal

import ollama
from ollama import ChatResponse, GenerateResponse


class OllamaResponseGenerator:
    model_name:str
    def __init__(self, model_name:str):
        self.model_name = model_name

    def generate(self, msgs:list[dict[Literal['role', 'content'], str]]) -> ChatResponse:
        response: ChatResponse = ollama.chat(model=self.model_name, messages=msgs)
        return response

    def generate_simple(self, prompt:str) -> str:
        response: ChatResponse = ollama.chat(model=self.model_name, messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        return response.message.get('content')

    def generate_with_image(self, prompt:str, image: str) -> str:
        response: GenerateResponse = ollama.generate(model=self.model_name, prompt=prompt, images=[image])
        return response.response
