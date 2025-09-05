from fastapi import APIRouter
from app.services.fantasy_service import get_fantasy

router = APIRouter(prefix="/nfl/fantasy", tags=["NFL Fantasy"])

@router.get("/")
def read_fantasy():
    return get_fantasy("nfl")
