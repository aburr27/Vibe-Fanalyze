# app/services/teams_services.py
from typing import List, Optional
from app.repositories.mysql_repo import TeamsRepository
from app.models.team import Team


def get_teams(sport: str) -> List[dict]:
    """
    Fetch all teams for a given sport from MySQL.
    """
    rows = TeamsRepository.get_teams(sport)
    return [Team(**row).dict() for row in rows]


def get_team_by_name(name: str, sport: str) -> Optional[dict]:
    """
    Fetch a single team by name from MySQL.
    """
    row = TeamsRepository.get_team_by_name(name, sport)
    return Team(**row).dict() if row else None
