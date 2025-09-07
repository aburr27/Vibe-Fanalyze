from fastapi import APIRouter
from app.services.games_services import get_games, get_game

router = APIRouter(prefix="/mlb/games", tags=["MLB Games"])

@router.get("/")
def fetch_mlb_games():
    return get_games("mlb")

@router.get("/{game_id}")
async def fetch_mlb_game(game_id: int):
    return await get_game("mlb", game_id)
