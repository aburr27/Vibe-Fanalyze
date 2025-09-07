from fastapi import APIRouter
from app.services.stats_services import get_stats

router = APIRouter(prefix="/nfl/stats", tags=["NFL Stats"])

@router.get("/{game_id}")
async def fetch_nfl_stats(game_id: int):
    return await get_stats("nfl", game_id)
