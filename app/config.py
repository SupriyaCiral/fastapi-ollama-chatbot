from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    MODEL_NAME: str = "llama3:8b"

settings = Settings()