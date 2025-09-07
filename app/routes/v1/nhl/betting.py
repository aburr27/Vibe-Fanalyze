from fastapi import APIRouter
from app.services.betting_services import get_betting

router = APIRouter(prefix="/nhl/betting", tags=["NHL Betting"])

@router.get("/{game_id}")
async def fetch_nhl_betting(game_id: int):
    return await get_betting("nhl", game_id)
