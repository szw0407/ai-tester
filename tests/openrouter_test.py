"""
This is the main program we choose to run for testing the models.

Although the models provided on OpenRouter is different from the ones
provided directly by OpenAI, Google, or Anthropic, but the APIs are
easier to be integrated, as it provides a unified API for different models.

This can also be modified to test other models in the openai-compatible
APIs, such as those provided by Poe or HuggingFace. You simply need to
overwrite `BASE_URL`.
"""

from OpenAICompatibleAPI import ResponseGenerator
from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam

BASE_URL = 'https://openrouter.ai/api/v1'

gpt5 = ResponseGenerator(
    model_name='openai/gpt-5',
    base_url=BASE_URL,
)

# now ask it to write a hello-world program in Python,
response = gpt5.generate(
    msgs=[ChatCompletionSystemMessageParam(content="You are a helpful assistant. You can only write Python code. Your code will then be executed directly. You must ensure the code is safe to run, and no extra word will be given, unless you have made sure that they are properly commented and makes no difference to the code execution at all. You are not allowed to write code that can harm the system. To keep code safe, you can only use built in things.", role="system"),
            ChatCompletionUserMessageParam(content="Write a program in Python to sort 1,2,45,4,43,99,45,12,35,6,54 by using HEAP.", role="user")

        ],
    temperature=0.1, max_tokens=51200,
)

code = response.choices[0].message.content

# now we use Python interpreter to execute the code
print("The code generated is:")
print(code)
# to keep everything safe, we will not use `eval` directly
# we will use as recommended, `exec` in a restricted namespace
# https://docs.python.org/3/library/functions.html#exec
while 1:
    try:
        exec(code)
    except Exception as e:
        # ask the model to fix the code, by giving the error message
        print(f"Error occurred: {e}")
        response = gpt5.generate(
            msgs=[ChatCompletionSystemMessageParam(content="You are a helpful assistant. You can only write Python code. Your code will then be executed directly. You must ensure the code is safe to run, and no extra word will be given, unless you have made sure that they are properly commented and makes no difference to the code execution at all. You are not allowed to write code that can harm the system.", role="system"),
                    ChatCompletionUserMessageParam(content=f"The following code has an error: {e}. Please fix it.\n```python\n{code}\n```", role="user")
                ],
            temperature=0.1, max_tokens=51200,
        )
        code = response.choices[0].message.content
        print("The code generated is:")
        print(code)
    else:
        break
print("The code executed successfully.")