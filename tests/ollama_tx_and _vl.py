from OllamaClient import OllamaResponseGenerator
from ImageTools import encode_image_to_base64, load_image
# import PIL
import httpx
from PIL.Image import Image
if __name__ == "__main__":
    generator = OllamaResponseGenerator("gpt-oss:20b")
    response = generator.generate_simple("What is the capital of France?")
    print(response)
    generator = OllamaResponseGenerator("qwen2.5vl:latest")
    # get an image from an Internet provider
    img:Image = load_image(
        "https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d"
    )
    img_base64 = encode_image_to_base64(img)
    prompt = f"Describe this image in detail"
    response = generator.generate_with_image(prompt, img_base64)
    print(response)
