from fastapi import APIRouter
from app.services.games_services import get_games, get_game

router = APIRouter(prefix="/nhl/games", tags=["NHL Games"])

@router.get("/")
def fetch_nhl_games():
    return get_games("nhl")

@router.get("/{game_id}")
async def fetch_nhl_game(game_id: int):
    return await get_game("nhl", game_id)