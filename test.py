from app.services.ollama_service import OllamaService
service = OllamaService()
answer = service.generate_response("What is the capital of France?")
print(answer)