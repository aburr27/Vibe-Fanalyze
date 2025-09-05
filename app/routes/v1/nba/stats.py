from fastapi import APIRouter
from app.services.stats_service import get_stats

router = APIRouter(prefix="/nba/stats", tags=["NBA Stats"])

@router.get("/")
def read_stats():
    return get_stats("nba")
