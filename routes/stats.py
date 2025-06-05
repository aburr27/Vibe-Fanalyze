from fastapi import APIRouter
from backend.models.player import Player

router = APIRouter(prefix="/stats", tags=["Stats"])

@router.get("/player/{player_id}")
def get_player_stats(player_id: int):
    # Placeholder response
    return {
        "player_id": player_id,
        "points": 22.3,
        "assists": 6.1,
        "rebounds": 7.4
    }
