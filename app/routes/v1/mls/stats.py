from fastapi import APIRouter
from app.services.stats_services import get_stats

router = APIRouter(prefix="/mls/stats", tags=["MLS Stats"])

@router.get("/{game_id}")
async def fetch_mls_stats(game_id: int):
    return await get_stats("mls", game_id)
