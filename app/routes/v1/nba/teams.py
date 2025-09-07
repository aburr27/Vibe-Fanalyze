from fastapi import APIRouter
from app.services.teams_services import get_teams, get_team_by_name

router = APIRouter(prefix="/nba/teams", tags=["NBA Teams"])

@router.get("/")
def fetch_nba_teams():
    return get_teams("nba")

@router.get("/{name}")
def fetch_mlb_team(name: str):
    return get_team_by_name(name, "nba")
