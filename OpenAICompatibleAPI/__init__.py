import base64
import os
from typing import Iterable
from openai import OpenAI
from openai.types.chat import ChatCompletionDeveloperMessageParam, ChatCompletionSystemMessageParam, \
    ChatCompletionUserMessageParam, ChatCompletionAssistantMessageParam, ChatCompletionToolMessageParam, \
    ChatCompletionFunctionMessageParam, ChatCompletion
from openai.types.responses import ToolParam, Response, WebSearchToolParam, ResponseInputTextParam, \
    EasyInputMessageParam, ResponseInputImageParam
from openai.types.responses.response_input_item_param import Message
from openai.types.shared_params import Reasoning


class ResponseGenerator:
    client:OpenAI
    model_name:str
    def __init__(self, model_name:str, base_url:str|None=None, key:str|None=None):
        self.model_name = model_name
        self.client = OpenAI(
                api_key=key or os.getenv("OPENAI_API_KEY"),
                base_url=base_url or os.getenv("OPENAI_BASE_URL","https://api.openai.com/v1")
            )

    def generate(self, msgs:Iterable[ChatCompletionDeveloperMessageParam | ChatCompletionSystemMessageParam | ChatCompletionUserMessageParam | ChatCompletionAssistantMessageParam | ChatCompletionToolMessageParam | ChatCompletionFunctionMessageParam], **kwargs) -> ChatCompletion:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=msgs,

            **kwargs
        )
        return response
    def response(self, input:str, image_base64:str| None = None)->Response:
        return self.client.responses.create(
            model=self.model_name,
            tools=[
                WebSearchToolParam(
                    type="web_search",
                )
            ],
            input = [
                Message(role="user", content=[ResponseInputTextParam(
                    type="input_text",
                    text=input,
                ),ResponseInputImageParam(
                    type="input_image",
                    image_url=f"data:image/jpeg;base64,{image_base64}",
                    detail="auto",
                )
                ] if image_base64 else [
                    ResponseInputTextParam(
                        type="input_text",
                        text=input
                    )
                ]),

            ]

        )