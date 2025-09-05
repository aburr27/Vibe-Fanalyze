from fastapi import APIRouter
from app.services.teams_service import get_teams

router = APIRouter(prefix="/nfl/teams", tags=["NFL Teams"])

@router.get("/")
def read_teams():
    return {"teams": get_teams("nfl")}
