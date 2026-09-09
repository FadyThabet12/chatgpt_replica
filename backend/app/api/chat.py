from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.db.mongo import create_conversation, list_conversations, get_conversation
from app.services.chat_service import chat

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    conversation_id: str
    message: str = Field(..., min_length=1)

@router.post("/conversations")
async def new_conversation():
    return {"id": await create_conversation()}

@router.get("/conversations")
async def conversations():
    return await list_conversations()

@router.get("/conversations/{conversation_id}")
async def conversation(conversation_id: str):
    doc = await get_conversation(conversation_id)
    if not doc:
        raise HTTPException(404, "Conversation not found")
    return doc

@router.post("/message")
async def message(req: ChatRequest):
    try:
        answer = await chat(req.conversation_id, req.message)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(500, str(e))
