from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

client = AsyncIOMotorClient(settings.MONGO_URL)
db = client.chatgpt_replica
conversations = db.conversations

def _serialize(doc):
    if not doc:
        return None
    doc["id"] = str(doc.pop("_id"))
    return doc

async def create_conversation(title="New chat"):
    result = await conversations.insert_one({"title": title, "messages": []})
    return str(result.inserted_id)

async def list_conversations():
    docs = []
    async for doc in conversations.find({}, {"messages": 0}).sort("_id", -1):
        docs.append(_serialize(doc))
    return docs

async def get_conversation(conversation_id):
    from bson import ObjectId
    return _serialize(await conversations.find_one({"_id": ObjectId(conversation_id)}))

async def add_message(conversation_id, message):
    from bson import ObjectId
    await conversations.update_one({"_id": ObjectId(conversation_id)}, {"$push": {"messages": message}})

async def rename_conversation(conversation_id, title):
    from bson import ObjectId
    await conversations.update_one({"_id": ObjectId(conversation_id)}, {"$set": {"title": title}})
