from fastapi import APIRouter, HTTPException
from backend.db.mongo_connector import mongo_db
from backend.models.game import Game

router = APIRouter(prefix="/games", tags=["Games"])

# Create
@router.post("/")
def create_game(game: Game):
    if mongo_db.games.find_one({"id": game.id}):
        raise HTTPException(status_code=400, detail="Game already exists.")
    mongo_db.games.insert_one(game.dict())
    return {"message": "Game created."}

# Read
@router.get("/{game_id}")
def get_game(game_id: int):
    game = mongo_db.games.find_one({"id": game_id}, {"_id": 0})
    if not game:
        raise HTTPException(status_code=404, detail="Game not found.")
    return game

# Update
@router.put("/{game_id}")
def update_game(game_id: int, updated: Game):
    result = mongo_db.games.update_one({"id": game_id}, {"$set": updated.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Game not found.")
    return {"message": "Game updated."}

# Delete
@router.delete("/{game_id}")
def delete_game(game_id: int):
    result = mongo_db.games.delete_one({"id": game_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Game not found.")
    return {"message": "Game deleted."}
