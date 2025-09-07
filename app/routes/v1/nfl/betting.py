from fastapi import APIRouter
from app.services.betting_services import get_betting

router = APIRouter(prefix="/nfl/betting", tags=["NFL Betting"])

@router.get("/{game_id}")
async def fetch_nfl_betting(game_id: int):
    return await get_betting("nfl", game_id)
