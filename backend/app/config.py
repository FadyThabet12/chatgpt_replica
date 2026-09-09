import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    LLM_API_KEY = os.getenv("LLM_API_KEY", "")
    LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
    MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql://postgres:postgres@localhost:5432/ragdb")
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

settings = Settings()
