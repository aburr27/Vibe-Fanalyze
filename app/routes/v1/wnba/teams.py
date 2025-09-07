from fastapi import APIRouter
from app.services.teams_services import get_teams, get_team_by_name

router = APIRouter(prefix="/wnba/teams", tags=["WNBA Teams"])

@router.get("/")
def fetch_nba_teams():
    return get_teams("wnba")

@router.get("/{name}")
def fetch_wnba_team(name: str):
    return get_team_by_name(name, "wnba")
