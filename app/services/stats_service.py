# app/services/stats_services.py
from typing import List
from app.repositories.mongo_repo import StatsRepository


async def get_stats(sport: str, game_id: int) -> List[dict]:
    """
    Fetch all player stats for a given game from MongoDB.
    """
    docs = await StatsRepository.get_for_game(sport, game_id)
    return [s.dict() for s in docs]
