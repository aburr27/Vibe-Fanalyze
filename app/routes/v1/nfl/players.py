from fastapi import APIRouter
from app.services.players_services import get_players, get_player_by_id

router = APIRouter(prefix="/nfl/players", tags=["NFL Players"])

@router.get("/")
async def fetch_nfl_players():
    return await get_players("nfl")

@router.get("/{player_id}")
async def fetch_nfl_player(player_id: int):
    return await get_player_by_id(player_id, "nfl")
