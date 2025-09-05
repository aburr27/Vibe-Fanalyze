from app.db.mysql_connector import mysql_conn
from app.db.mongo_connector import mongo_client
from app.models.games import Game

betting_collection = mongo_client['vibe_fanalyze_db']['betting']

def get_game(sport: str, game_id: int):
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM games WHERE sport=%s AND id=%s", (sport.lower(), game_id))
    game_row = cursor.fetchone()
    cursor.close()
    
    if game_row:
        game = Game(**game_row)
        # Fetch betting data from Mongo
        bet_doc = betting_collection.find_one({"sport": sport.lower(), "game_id": game_id})
        if bet_doc:
            game.bet = bet_doc  # optional field in Game model
        return game.dict()
    return None
