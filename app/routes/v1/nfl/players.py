from fastapi import APIRouter
from app.services.players_service import get_players

router = APIRouter(prefix="/nfl/players", tags=["NFL Players"])

@router.get("/")
def read_players():
    return {"players": get_players("nfl")}
