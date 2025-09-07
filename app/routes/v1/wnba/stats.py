from fastapi import APIRouter
from app.services.stats_services import get_stats

router = APIRouter(prefix="/wnba/stats", tags=["WNBA Stats"])

@router.get("/{game_id}")
async def fetch_wnba_stats(game_id: int):
    return await get_stats("wnba", game_id)
