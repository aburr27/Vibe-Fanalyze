from fastapi import APIRouter
from app.services.stats_services import get_stats

router = APIRouter(prefix="/nhl/stats", tags=["NHL Stats"])

@router.get("/{game_id}")
async def fetch_nhl_stats(game_id: int):
    return await get_stats("nhl", game_id)
