from fastapi import APIRouter
from app.services.games_service import get_games, get_game
from app.services.betting_service import get_betting

router = APIRouter(prefix="/nfl/games", tags=["NFL Games"])

@router.get("/")
def read_games():
    return {"games": get_games("nfl")}

@router.get("/{game_id}")
def read_game(game_id: int):
    game = get_game("nfl", game_id)
    if not game:
        return {"error": "Game not found"}
    return game

@router.get("/{game_id}/betting")
def read_betting(game_id: int):
    return get_betting("nfl", game_id)
