from fastapi import APIRouter
from app.services.games_services import get_games, get_game

router = APIRouter(prefix="/nfl/games", tags=["NFL Games"])

@router.get("/")
def fetch_nfl_games():
    return get_games("nfl")

@router.get("/{game_id}")
async def fetch_nfl_game(game_id: int):
    return await get_game("nfl", game_id)