from google.genai.types import GenerateImagesConfig, GenerateImagesResponse, GeneratedImage
from typing_extensions import override

from . import GeminiResponseGenerator

class GeminiImagenGenerator(GeminiResponseGenerator):
    def __init__(self, model_name: str = "imagen-4.0-generate-001"):
        super().__init__(model_name=model_name)

    @override
    def generate(self, prompt:str, config:GenerateImagesConfig=None) -> GenerateImagesResponse:
        return self.client.models.generate_images(
            model=self.model_name,
            prompts=[prompt],
            config=config
        )

    def generate_images(self, prompt, count: int = 4, **kwargs) -> list[GeneratedImage]:
        """
        A simple interface to generate and display images based on a prompt.
        This method generates 'count' images based on the provided prompt and any additional
        configuration parameters passed via kwargs. The generated images are displayed using
        the default image viewer and returned as a list of PIL ImageFile objects.

        :param prompt:
        :param count:
        :param kwargs:
        :return:
        """
        images = self.generate(
            prompt,
            config=GenerateImagesConfig(
                number_of_images=count,
                **kwargs
            )
        ).generated_images
        for image in images:
            image.show()
        return images

