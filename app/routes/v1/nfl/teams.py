from fastapi import APIRouter
from app.services.teams_services import get_teams, get_team_by_name

router = APIRouter(prefix="/nfl/teams", tags=["NFL Teams"])

@router.get("/")
def fetch_nfl_teams():
    return get_teams("nfl")

@router.get("/{name}")
def fetch_nfl_team(name: str):
    return get_team_by_name(name, "nfl")
