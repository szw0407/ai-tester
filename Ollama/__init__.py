from typing import Literal

from ollama import chat
from ollama import ChatResponse

class OllamaResponseGenerator:
    model_name:str
    def __init__(self, model_name:str):
        self.model_name = model_name

    def generate(self, msgs:list[dict[Literal['role', 'content'], str]]) -> ChatResponse:
        response: ChatResponse = chat(model=self.model_name, messages=msgs)
        return response

    def generate_simple(self, prompt:str) -> ChatResponse:
        response: ChatResponse = chat(model=self.model_name, messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        return response.messages.content


