from fastapi import APIRouter
from app.services.teams_services import get_teams, get_team_by_name

router = APIRouter(prefix="/mls/teams", tags=["MLS Teams"])

@router.get("/")
def fetch_mls_teams():
    return get_teams("mls")

@router.get("/{name}")
def fetch_mls_team(name: str):
    return get_team_by_name(name, "mls")
