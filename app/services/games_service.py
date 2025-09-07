# app/services/games_services.py
from typing import List, Optional
from app.repositories.mysql_repo import GamesRepository
from app.repositories.mongo_repo import BettingRepository
from app.models.game import Game

def get_games(sport: str) -> List[dict]:
    """
    Fetch all games for a sport from MySQL.
    """
    rows = GamesRepository.get_games(sport)
    return [Game(**row).dict() for row in rows]


async def get_game(sport: str, game_id: int) -> Optional[dict]:
    """
    Fetch a single game by ID from MySQL and enrich with betting from Mongo.
    """
    row = GamesRepository.get_game_by_id(game_id, sport)
    if row:
        game = Game(**row)
        bet_docs = await BettingRepository.get_for_game(sport, game_id)
        if bet_docs:
            game.betting = [b.dict() for b in bet_docs]
        return game.dict()
    return None
