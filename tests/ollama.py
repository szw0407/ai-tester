from Ollama import OllamaResponseGenerator

if __name__ == "__main__":
    generator = OllamaResponseGenerator("gpt-oss:20b")
    response = generator.generate_simple("What is the capital of France?")
    print(response)
    generator = OllamaResponseGenerator("qwen2.5vl:latest")
