from fastapi import APIRouter
from app.services.players_services import get_players, get_player_by_id

router = APIRouter(prefix="/nhl/players", tags=["NHL Players"])

@router.get("/")
async def fetch_nhl_players():
    return await get_players("nhl")

@router.get("/{player_id}")
async def fetch_nhl_player(player_id: int):
    return await get_player_by_id(player_id, "nhl")
