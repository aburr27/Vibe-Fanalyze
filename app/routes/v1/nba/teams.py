from fastapi import APIRouter
from app.services.teams_service import get_teams

router = APIRouter(prefix="/nba/teams", tags=["NBA Teams"])

@router.get("/")
def read_teams():
    return {"teams": get_teams("nba")}
