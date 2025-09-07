# app/services/players_services.py
from typing import List, Optional
from app.repositories.mongo_repo import PlayerRepository


async def get_players(sport: str) -> List[dict]:
    """
    Fetch all players for a given sport from MongoDB.
    """
    docs = await PlayerRepository.get_all(sport)
    return [p.dict() for p in docs]


async def get_player_by_id(player_id: int, sport: str) -> Optional[dict]:
    """
    Fetch a single player by ID from MongoDB.
    """
    doc = await PlayerRepository.get_by_id(player_id, sport)
    return doc.dict() if doc else None
