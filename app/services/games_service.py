from app.db.mysql_connector import mysql_conn
from app.db.mongo_connector import mongo_client
from app.models.games import Game

betting_collection = mongo_client['vibe_fanalyze_db']['betting']

def get_games(sport: str):
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT games.* FROM games
        JOIN sports ON games.sport_id = sports.id
        WHERE LOWER(sports.name) = %s
    """, (sport.lower(),))
    rows = cursor.fetchall()
    cursor.close()
    return [Game(**row).dict() for row in rows]

def get_game(sport: str, game_id: int):
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT games.* FROM games
        JOIN sports ON games.sport_id = sports.id
        WHERE LOWER(sports.name) = %s AND games.id = %s
    """, (sport.lower(), game_id))
    row = cursor.fetchone()
    cursor.close()
    if row:
        game = Game(**row)
        # Add betting info from Mongo
        bet_doc = betting_collection.find_one({"sport": sport.lower(), "game_id": game_id})
        if bet_doc:
            game.bet = bet_doc  # optional field in Game model
        return game.dict()
    return None
