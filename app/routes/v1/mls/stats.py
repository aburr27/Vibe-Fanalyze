from fastapi import APIRouter, HTTPException
from fastapi import APIRouter
from app.db.mongo_connector import mongo_db
from app.utils.fantasy_points import calculate_fantasy_points
from app.models.player import Player

router = APIRouter(prefix="/stats", tags=["Stats"])

@router.get("/player/{player_id}", response_model=dict)
def get_player_stats(player_id: int):
    player = mongo_db.players.find_one({"player_id": player_id})
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    stats = player.get("stats", {})
    fantasy_score = calculate_fantasy_points(stats, league="NBA")
    
    return {
        "player_id": player_id,
        "name": player.get("name", ""),
        "team": player.get("team", ""),
        "position": player.get("position", ""),
        "stats": stats,
        "fantasy_points": round(fantasy_score, 2)
    }
