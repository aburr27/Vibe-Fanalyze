from fastapi import APIRouter
from app.services.players_services import get_players, get_player_by_id

router = APIRouter(prefix="/wnba/players", tags=["WNBA Players"])

@router.get("/")
async def fetch_wnba_players():
    return await get_players("wnba")

@router.get("/{player_id}")
async def fetch_wnba_player(player_id: int):
    return await get_player_by_id(player_id, "wnba")
