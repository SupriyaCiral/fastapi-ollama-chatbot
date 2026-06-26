from fastapi import FastAPI
from app.services.ollama_service import OllamaService
from app.models.schemas import QuestionRequest, QuestionResponse


ollama_service = OllamaService()
app = FastAPI()

@app.post("/ask")
def ask(request: QuestionRequest):

    answer = ollama_service.generate_response(
        request.question
    )

    return QuestionResponse(
        question=request.question,
        answer=answer
    )

@app.get("/")
def read_root():
    return {"message": "hello World"}