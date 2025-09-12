from Gemini.MultiModalReader import GeminiMultiModalQA
from httpx import URL
from PIL import Image
if __name__ == "__main__":
    reader = GeminiMultiModalQA(model_name="gemini-2.5-flash")
    # Read an image from a URL
    image_url = URL("https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d")
    question = "Describe this image in detail."
    answer = reader.generate_with_image(question, image_url)
    print("Answer from image URL:", answer)

    # Read an image from a local file
    local_image_path = "tests/temp.png"  # Replace with your local image path
    img = Image.open(local_image_path)
    question = "What is shown in this image?"
    print("Answer from local image file:", answer)