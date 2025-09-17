"""
第一个测试：对于一个图片的地点寻找有关信息

"""
from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionContentPartTextParam, \
    ChatCompletionContentPartImageParam
from openai.types.chat.chat_completion_content_part_image_param import ImageURL


from OpenAICompatibleAPI import ResponseGenerator
from ImageTools import encode_image_to_base64
gpt5 = ResponseGenerator("openai/gpt-5:online", base_url="https://openrouter.ai/api/v1")
gemini_2_5_pro = ResponseGenerator("google/gemini-2.5-pro:online", base_url="https://openrouter.ai/api/v1")

QUESTION = "This is a photo taken outside a museum in 浦河町. Some tourists want to visit the place to visit. They will visit the museum on Wednesday and leave immediately at the time the museum closes. Then they will go to the nearest bus transportation station immediately. We suggest that everything will go as expected including the train schedule and the museum opening hours and the expected walking duration. Please tell me the destination of the first bus to meet in the station. You need to search the Internet and find the answer and you can briefly introduce how you gained that information if you like."

base64_image=encode_image_to_base64("Images/image_one.png")
# now we can test the GPT5 or Gemini performance in this problem
answer = gemini_2_5_pro.generate(
    msgs=[
        ChatCompletionUserMessageParam(
            content=[
                ChatCompletionContentPartTextParam(text=QUESTION),
                ChatCompletionContentPartImageParam(image_url=ImageURL(url="data:image/png;base64,"+base64_image), type="image_url"),
            ],
            role="user"
        )
    ],
)

print("The answer from Gemini is:")
print(answer.choices[0].message.content)
