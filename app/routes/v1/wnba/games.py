from fastapi import APIRouter
from app.services.games_services import get_games, get_game

router = APIRouter(prefix="/wnba/games", tags=["WNBA Games"])

@router.get("/")
def fetch_wnba_games():
    return get_games("wnba")

@router.get("/{game_id}")
async def fetch_wnba_game(game_id: int):
    return await get_game("wnba", game_id)