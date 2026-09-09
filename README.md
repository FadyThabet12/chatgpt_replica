# ChatGPT Replica — Production RAG Architecture

A ChatGPT-style application built using the same modular, production-oriented ideas as the provided ML/RAG notebook: API layer, databases, vector search, background processing, logging, Docker orchestration, and a separate frontend.

## Architecture

- **Frontend:** React + Vite
- **Backend:** FastAPI
- **LLM:** OpenAI-compatible chat endpoint (provider configurable through `.env`)
- **Chat history:** MongoDB
- **RAG/vector search:** PostgreSQL + pgvector + Sentence Transformers
- **Background document processing:** Celery + Redis
- **Uploads:** local `uploads/` volume
- **Deployment:** Docker Compose

## Structure

```text
chatgpt-replica/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── chat.py
│   │   │   ├── files.py
│   │   │   └── health.py
│   │   ├── db/
│   │   │   ├── mongo.py
│   │   │   └── vector_db.py
│   │   ├── services/
│   │   │   ├── llm.py
│   │   │   ├── rag.py
│   │   │   └── chat_service.py
│   │   ├── utils/
│   │   │   ├── chunking.py
│   │   │   ├── embeddings.py
│   │   │   └── text_extraction.py
│   │   ├── celery_app.py
│   │   ├── config.py
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Sidebar.jsx
│   │   │   ├── ChatWindow.jsx
│   │   │   └── MessageInput.jsx
│   │   ├── pages/Chat.jsx
│   │   ├── services/api.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles.css
│   ├── package.json
│   └── Dockerfile
├── uploads/
├── docker-compose.yml
└── .env.example
```

## Run

1. Copy `.env.example` to `.env` and add your LLM API key.
2. Run `docker compose up --build`.
3. Open the frontend at `http://localhost:5173`.
4. API docs: `http://localhost:8000/docs`.

The application supports conversations, chat history, document upload, RAG retrieval, and a ChatGPT-like interface.
