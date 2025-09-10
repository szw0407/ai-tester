from Gemini.nano_banana_image import GeminiImageGenerator
from Gemini.Imagen import GeminiImagenGenerator
from Gemini.text_response import GeminiTextGenerator
from uuid import uuid4
if __name__ == "__main__":
    try:
        prompt = "How do AI work?"
        text_generator = GeminiTextGenerator()
        response = text_generator.simple_chat(prompt, enable_think=False)
        print("Text response:", response)
    except Exception as e:
        print("Error during text generation:", e)
        print("Text generation failed")

    prompt = "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
    try:
        image_generator = GeminiImagenGenerator()
        image = image_generator.generate_images(
            prompt,
            count=1,
        )
        for img in image:
            img.save(f"generated_image_{uuid4().hex}.png")
        print("Image generation successful, saved"+  f" {len(image)} images.")
    except Exception as e:
        print("Error during image generation:", e)
        print("Imagen generation failed")
    try:
        image_generator = GeminiImageGenerator()
        image = image_generator.generate_image(prompt)
        if image:
            image.show()
            image.save(f"generated_image_{uuid4().hex}.png")
        else:
            print("No image generated.")
    except Exception as e:
        print("Error during nano banana image generation:", e)
        print("Nano banana image generation failed")

