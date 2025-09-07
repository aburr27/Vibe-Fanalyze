from fastapi import APIRouter
from app.services.stats_services import get_stats

router = APIRouter(prefix="/mlb/stats", tags=["MLB Stats"])

@router.get("/{game_id}")
async def fetch_mlb_stats(game_id: int):
    return await get_stats("mlb", game_id)
