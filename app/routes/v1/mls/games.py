from fastapi import APIRouter
from app.services.games_services import get_games, get_game

router = APIRouter(prefix="/mls/games", tags=["MLS Games"])

@router.get("/")
def fetch_mls_games():
    return get_games("mls")

@router.get("/{game_id}")
async def fetch_mls_game(game_id: int):
    return await get_game("mls", game_id)