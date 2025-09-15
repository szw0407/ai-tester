import os
from typing import Iterable
from openai import OpenAI
from openai.types.chat import ChatCompletionDeveloperMessageParam, ChatCompletionSystemMessageParam, \
    ChatCompletionUserMessageParam, ChatCompletionAssistantMessageParam, ChatCompletionToolMessageParam, \
    ChatCompletionFunctionMessageParam, ChatCompletion


class ResponseGenerator:
    client:OpenAI
    model_name:str
    def __init__(self, model_name:str, base_url:str|None=None, key:str|None=None):
        self.model_name = model_name
        self.client = OpenAI(
                api_key=key or os.getenv("OPENAI_API_KEY"),
                base_url=base_url or os.getenv("OPENAI_API_BASE_URL","https://api.openai.com/v1")
            )

    def generate(self, msgs:Iterable[ChatCompletionDeveloperMessageParam | ChatCompletionSystemMessageParam | ChatCompletionUserMessageParam | ChatCompletionAssistantMessageParam | ChatCompletionToolMessageParam | ChatCompletionFunctionMessageParam], **kwargs) -> ChatCompletion:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=msgs,
            **kwargs
        )
        return response

