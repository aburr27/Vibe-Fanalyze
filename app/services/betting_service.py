# app/services/betting_services.py
from typing import Dict, List
from app.repositories.mongo_repo import BettingRepository


async def get_betting(sport: str, game_id: int) -> List[Dict]:
    """
    Returns betting info for a given sport and game_id.
    """
    bets = await BettingRepository.get_for_game(sport, game_id)
    return [b.dict() for b in bets] if bets else [{"error": "No betting data for this game"}]
