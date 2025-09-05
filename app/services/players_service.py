from app.db.mongo_connector import mongo_client
from app.db.mysql_connector import mysql_conn
from app.models.players import Player

players_collection = mongo_client['vibe_fanalyze_db']['players']

def get_players(sport: str):
    # MongoDB fetch
    docs = players_collection.find({"sport": sport.lower()})
    return [Player(**doc).dict() for doc in docs]

def get_player_by_id(player_id: int, sport: str):
    doc = players_collection.find_one({"id": player_id, "sport": sport.lower()})
    if doc:
        return Player(**doc).dict()
    return None
