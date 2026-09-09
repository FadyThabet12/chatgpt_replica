import httpx
from app.config import settings

async def generate_answer(messages, context=""):
    system = "You are a helpful AI assistant. Answer clearly and accurately."
    if context:
        system += "\nUse the following retrieved context when relevant:\n" + context
    payload = {
        "model": settings.LLM_MODEL,
        "messages": [{"role": "system", "content": system}] + messages,
        "temperature": 0.2,
    }
    headers = {"Authorization": f"Bearer {settings.LLM_API_KEY}"}
    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post(f"{settings.LLM_BASE_URL}/chat/completions", json=payload, headers=headers)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
