from fastapi import APIRouter
from app.services.teams_services import get_teams, get_team_by_name

router = APIRouter(prefix="/nhl/teams", tags=["NHL Teams"])

@router.get("/")
def fetch_nhl_teams():
    return get_teams("nhl")

@router.get("/{name}")
def fetch_nhl_team(name: str):
    return get_team_by_name(name, "nhl")
