from fastapi import APIRouter
from app.services.players_services import get_players, get_player_by_id

router = APIRouter(prefix="/mlb/players", tags=["MLB Players"])

@router.get("/")
async def fetch_mlb_players():
    return await get_players("mlb")

@router.get("/{player_id}")
async def fetch_mlb_player(player_id: int):
    return await get_player_by_id(player_id, "mlb")
