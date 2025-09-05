from app.db.mongo_connector import mongo_client
from app.models.fantasy import Fantasy

fantasy_collection = mongo_client['vibe_fanalyze_db']['fantasy']

def get_fantasy(sport: str):
    doc = fantasy_collection.find_one({"sport": sport.lower()})
    if doc:
        return Fantasy(**doc).dict()
    return {}
