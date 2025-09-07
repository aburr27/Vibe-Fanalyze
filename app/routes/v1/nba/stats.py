from fastapi import APIRouter
from app.services.stats_services import get_stats

router = APIRouter(prefix="/nba/stats", tags=["NBA Stats"])

@router.get("/{game_id}")
async def fetch_nba_stats(game_id: int):
    return await get_stats("nba", game_id)
