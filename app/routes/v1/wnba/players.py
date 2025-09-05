from fastapi import APIRouter, HTTPException
from app.db.mongo_connector import mongo_db
from app.models.player import Player
router = APIRouter(prefix="/players", tags=["Players"])

PLAYER_NOT_FOUND_MSG = "Player not found."

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
    player = mongo_db.players.find_one({"id": player_id})
    if not player:
        raise HTTPException(status_code=404, detail=PLAYER_NOT_FOUND_MSG)
    player["_id"] = str(player["_id"])  # Convert ObjectId to string if needed
    return player

# Update
@router.put("/{player_id}")
def update_player(player_id: int, player: Player):
    result = mongo_db.players.update_one({"id": player_id}, {"$set": player.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail=PLAYER_NOT_FOUND_MSG)
    return {"message": "Player updated."}

# Delete
@router.delete("/{player_id}")
def delete_player(player_id: int):
    result = mongo_db.players.delete_one({"id": player_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail=PLAYER_NOT_FOUND_MSG)
    return {"message": "Player deleted."}
