from fastapi import APIRouter
from app.services.players_services import get_players, get_player_by_id

router = APIRouter(prefix="/nba/players", tags=["NBA Players"])

@router.get("/")
async def fetch_nba_players():
    return await get_players("nba")

@router.get("/{player_id}")
async def fetch_nba_player(player_id: int):
    return await get_player_by_id(player_id, "nba")
