from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.chat import router as chat_router
from app.api.files import router as files_router
from app.api.health import router as health_router

app = FastAPI(title="ChatGPT Replica API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=[settings.FRONTEND_URL], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(chat_router, prefix="/api/v1")
app.include_router(files_router, prefix="/api/v1")
app.include_router(health_router)

@app.get("/")
def root():
    return {"message": "ChatGPT Replica API"}
