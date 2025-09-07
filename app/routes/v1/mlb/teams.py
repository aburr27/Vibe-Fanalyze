from fastapi import APIRouter
from app.services.teams_services import get_teams, get_team_by_name

router = APIRouter(prefix="/mlb/teams", tags=["MLB Teams"])

@router.get("/")
def fetch_mlb_teams():
    return get_teams("mlb")

@router.get("/{name}")
def fetch_mlb_team(name: str):
    return get_team_by_name(name, "mlb")
