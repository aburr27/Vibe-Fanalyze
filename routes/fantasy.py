from fastapi import APIRouter, HTTPException
from backend.db.mongo_connector import mongo_db
from backend.fantasy_points import calculate_fantasy_points

router = APIRouter(prefix="/fantasy", tags=["Fantasy"])

@router.get("/player/{player_id}")
def get_fantasy_points(player_id: int):
    player = mongo_db.players.find_one({"id": player_id}, {"_id": 0})
    if not player:
        raise HTTPException(status_code=404, detail="Player not found.")

    league = player.get("league", "NBA")  # Default NBA if not set
    stats = player.get("stats", {})
    points = calculate_fantasy_points(stats, league)
    return {"player_id": player_id, "fantasy_points": points}
    
