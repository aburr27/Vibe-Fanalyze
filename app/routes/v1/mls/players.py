from fastapi import APIRouter
from app.services.players_services import get_players, get_player_by_id

router = APIRouter(prefix="/mls/players", tags=["MLS Players"])

@router.get("/")
async def fetch_mls_players():
    return await get_players("mls")

@router.get("/{player_id}")
async def fetch_mls_player(player_id: int):
    return await get_player_by_id(player_id, "mls")
