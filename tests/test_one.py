import google.genai.types
from google.genai.types import GenerateContentConfig, ThinkingConfig, GoogleSearch

import OpenAICompatibleAPI

gpt5 = OpenAICompatibleAPI.ResponseGenerator("gpt-5")

import Gemini.MultiModalReader

gemini2_5_pro = Gemini.MultiModalReader.GeminiMultiModalQA("gemini-2.5-pro")

QUESTION = "This is a photo taken in 浦河町 beside a museum. Find the location and tell me, if we visit it on Wednesday leave at the time it closes by taking a bus at the nearest stop, the destination of the first bus we will meet there."
from ImageTools import encode_image_to_base64, load_image
# load image
image_base64=encode_image_to_base64("Images/image_one.png", (1280,720))
image_file=load_image("Images/image_one.png")
# generate response
response = gpt5.response(
    input=QUESTION,
    image_base64=image_base64
)

print(response)

# save response to pkl file

import pickle

with open('openai.pkl', 'wb') as f:
    pickle.dump(response, f)

# now test gemini

response2 = gemini2_5_pro.generate_with_image(QUESTION, image_file, GenerateContentConfig(
    thinking_config=ThinkingConfig(
        thinking_budget=-1,  # auto
include_thoughts=True
    ),
    tools=[
        google.genai.types.Tool(google_search=GoogleSearch())
    ]
))

print(response2.text)

with open("Google.pkl", "wb") as f:
    pickle.dump(response2, f)


