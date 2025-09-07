from fastapi import APIRouter
from app.services.betting_services import get_betting

router = APIRouter(prefix="/nba/betting", tags=["NBA Betting"])

@router.get("/{game_id}")
async def fetch_nba_betting(game_id: int):
    return await get_betting("nba", game_id)
