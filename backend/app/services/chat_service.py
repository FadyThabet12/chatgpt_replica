from app.db.mongo import add_message, get_conversation
from app.services.llm import generate_answer
from app.services.rag import retrieve

async def chat(conversation_id, user_text):
    conversation = await get_conversation(conversation_id)
    history = conversation.get("messages", [])[-12:]
    context = retrieve(user_text) if user_text.strip() else ""
    answer = await generate_answer(history + [{"role": "user", "content": user_text}], context)
    await add_message(conversation_id, {"role": "user", "content": user_text})
    await add_message(conversation_id, {"role": "assistant", "content": answer})
    return answer
