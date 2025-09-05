from fastapi import APIRouter
from app.services.stats_service import get_stats

router = APIRouter(prefix="/nfl/stats", tags=["NFL Stats"])

@router.get("/")
def read_stats():
    return get_stats("nfl")
