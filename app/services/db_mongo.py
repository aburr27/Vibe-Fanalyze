"""
MongoDB Database Connection for Vibe-Fanalyze
Stores chat history and unstructured analytics.
"""

from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "vibefanalyze")

client = AsyncIOMotorClient(MONGO_URI)
mongo_db = client[MONGO_DB]

async def save_chat_log(user_msg: str, bot_response: str, data: dict = None):
    """Save chat conversation in MongoDB."""
    chat_entry = {
        "user_message": user_msg,
        "bot_response": bot_response,
        "data": data or {},
    }
    await mongo_db.chat_logs.insert_one(chat_entry)

async def get_recent_chats(limit: int = 10):
    """Retrieve recent chat logs."""
    chats = mongo_db.chat_logs.find().sort("_id", -1).limit(limit)
    return [c async for c in chats]
