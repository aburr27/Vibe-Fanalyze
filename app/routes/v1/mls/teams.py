from fastapi import APIRouter, HTTPException
from fastapi import APIRouter
from backend.db.mongo_connector import mongo_db
from backend.models.team import Team

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.get("/")
def list_teams():
    return [{"id": 1, "name": "Team A"}]

@router.post("/")
def create_team(team: Team):
    if mongo_db.teams.find_one({"id": team.id}):
        raise HTTPException(status_code=400, detail="Team already exists.")
    mongo_db.teams.insert_one(team.dict())
    return {"message": "Team created."}

@router.get("/{team_id}")
def get_team(team_id: int):
    team = mongo_db.teams.find_one({"id": team_id}, {"_id": 0})
    if not team:
        raise HTTPException(status_code=404, detail="Team not found.")
    return team

@router.put("/{team_id}")
def update_team(team_id: int, updated: Team):
    result = mongo_db.teams.update_one({"id": team_id}, {"$set": updated.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Team not found.")
    return {"message": "Team updated."}

@router.delete("/{team_id}")
def delete_team(team_id: int):
    result = mongo_db.teams.delete_one({"id": team_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Team not found.")
    return {"message": "Team deleted."}

