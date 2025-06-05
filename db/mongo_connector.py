from pymongo import MongoClient
from backend.config import settings

client = MongoClient(settings.MONGO_URL)
mongo_db = client["sportsbot"]
