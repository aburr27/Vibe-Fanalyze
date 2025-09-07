from fastapi import APIRouter
from app.services.betting_services import get_betting

router = APIRouter(prefix="/mls/betting", tags=["MLS Betting"])

@router.get("/{game_id}")
async def fetch_mls_betting(game_id: int):
    return await get_betting("mls", game_id)
