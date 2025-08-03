from pymongo import MongoClient
from app.config.settings import settings

# Initialize MongoDB client using URI from settings
client = MongoClient(settings.MONGO_URL)

# Choose the database (adjust name if needed)
mongo_db = client.get_database("vibe_fanalyze")  # or "sportsdb" if that’s your preferred name
