from fastapi import APIRouter
from app.services.fantasy_service import get_fantasy

router = APIRouter(prefix="/nba/fantasy", tags=["NBA Fantasy"])

@router.get("/")
def read_fantasy():
    return get_fantasy("nba")
