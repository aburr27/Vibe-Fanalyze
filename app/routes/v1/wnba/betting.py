from fastapi import APIRouter
from app.services.betting_services import get_betting

router = APIRouter(prefix="/wnba/betting", tags=["WNBA Betting"])

@router.get("/{game_id}")
async def fetch_wnba_betting(game_id: int):
    return await get_betting("wnba", game_id)
