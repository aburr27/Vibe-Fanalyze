from fastapi import APIRouter
from app.services.games_service import get_games, get_game
from app.services.betting_service import get_betting

router = APIRouter(prefix="/nba/games", tags=["NBA Games"])

@router.get("/")
def read_games():
    return {"games": get_games("nba")}

@router.get("/{game_id}")
def read_game(game_id: int):
    game = get_game("nba", game_id)
    if not game:
        return {"error": "Game not found"}
    return game

@router.get("/{game_id}/betting")
def read_betting(game_id: int):
    return get_betting("nba", game_id)
