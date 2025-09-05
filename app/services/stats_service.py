from app.db.mongo_connector import mongo_client
from app.models.stats import Stat

stats_collection = mongo_client['vibe_fanalyze_db']['stats']

def get_stats(sport: str):
    doc = stats_collection.find_one({"sport": sport.lower()})
    if doc:
        return Stat(**doc).dict()
    return {}
