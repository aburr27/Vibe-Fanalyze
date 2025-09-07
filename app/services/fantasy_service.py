# app/services/fantasy_services.py
from typing import Optional
from app.repositories.mongo_repo import FantasyRepository


async def get_fantasy(sport: str, player_id: int) -> Optional[dict]:
    """
    Get fantasy stats for a player in a given sport.
    """
    doc = await FantasyRepository.get_for_player(player_id, sport)
    return doc.dict() if doc else {}
