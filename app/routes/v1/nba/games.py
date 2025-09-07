from fastapi import APIRouter
from app.services.games_services import get_games, get_game

router = APIRouter(prefix="/nba/games", tags=["NBA Games"])

@router.get("/")
def fetch_nba_games():
    return get_games("nba")

@router.get("/{game_id}")
async def fetch_nba_game(game_id: int):
    return await get_game("nba", game_id)
