from . import GeminiResponseGenerator
from google.genai import types

class GeminiTextGenerator(GeminiResponseGenerator):
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        super().__init__(model_name=model_name)

    def generate_text(self, prompt:str, config:types.GenerateContentConfig) -> str:
        response:types.GenerateContentResponse = self.generate(prompt, config=config)
        return response.text

    def simple_chat(self, prompt:str, enable_think : bool = True, **kwargs) -> str:
        """
        A simple chat interface that allows you to enable or disable the "think" feature.
        By default, Gemini models "think" before answering. If you want to disable this behavior,
        set enable_think to False. If a detailed thinking_config is provided in kwargs,
        it will override the enable_think setting.

        This methods only shows the output text, potential generated images or other media are ignored.
        Thoughts are not shown either.

        :param prompt:
        :param enable_think:
        :param kwargs:
        :return:
        """
        # the default behavior of Gemini is to "think" before answering
        config = types.GenerateContentConfig(**kwargs)
        if not enable_think and (not config.thinking_config or not config.thinking_config.thinking_budget):
            config.thinking_config = types.ThinkingConfig(thinking_budget=1000)

        return self.generate_text(prompt, config=config)
