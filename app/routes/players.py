from fastapi import APIRouter, HTTPException
from fastapi import APIRouter
from backend.db.mongo_connector import mongo_db
from backend.models.player import Player

router = APIRouter(prefix="/players", tags=["Players"])

@router.get("/")
def list_players():
    return [{"id": 1, "name": "Player A"}]

# Create
@router.post("/")
def create_player(player: Player):
    if mongo_db.players.find_one({"id": player.id}):
        raise HTTPException(status_code=400, detail="Player already exists.")
    mongo_db.players.insert_one(player.dict())
    return {"message": "Player created."}

# Read
@router.get("/{player_id}")
def get_player(player_id: int):
    player = mongo_db.players.find_one({"id": player_id}, {"_id": 0})
    if not player:
        raise HTTPException(status_code=404, detail="Player not found.")
    return player

# Update
@router.put("/{player_id}")
def update_player(player_id: int, updated: Player):
    result = mongo_db.players.update_one({"id": player_id}, {"$set": updated.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Player not found.")
    return {"message": "Player updated."}

# Delete
@router.delete("/{player_id}")
def delete_player(player_id: int):
    result = mongo_db.players.delete_one({"id": player_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Player not found.")
    return {"message": "Player deleted."}
