from fastapi import APIRouter
from app.services.betting_services import get_betting

router = APIRouter(prefix="/mlb/betting", tags=["MLB Betting"])

@router.get("/{game_id}")
async def fetch_mlb_betting(game_id: int):
    return await get_betting("mlb", game_id)
