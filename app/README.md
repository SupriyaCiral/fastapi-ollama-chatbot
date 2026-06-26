# 🤖 FastAPI Ollama Chatbot

An AI chatbot built using **FastAPI** and **Ollama** that runs Large Language Models (LLMs) locally without relying on cloud APIs.

---

## 🚀 Features

- FastAPI REST API
- Local LLM integration using Ollama
- Supports Llama 3 and Qwen models
- Request & Response validation using Pydantic
- Modular project architecture
- Structured logging
- Swagger UI documentation

---

## 🛠 Tech Stack

- Python
- FastAPI
- Uvicorn
- Ollama
- Llama 3
- Qwen2.5 Coder
- HTTPX
- Pydantic

---

## 📂 Project Structure

```
app
│
├── core
├── models
├── services
├── config.py
└── main.py
```

---

## Installation

```bash
git clone https://github.com/<your-username>/FastAPI-Ollama-Chatbot.git

cd FastAPI-Ollama-Chatbot

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## Run

```bash
python -m uvicorn app.main:app --reload
```

---

## API Documentation

Open

```
http://127.0.0.1:8000/docs
```

---

## Sample Request

```json
{
  "question": "Explain Retrieval-Augmented Generation"
}
```

---

## Future Enhancements

- Streaming responses
- Conversation memory
- React frontend
- Docker deployment
- Authentication