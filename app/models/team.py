from beanie import Document
from pydantic import BaseModel
from typing import Optional, Dict

class Stadium(BaseModel):
    name: str
    capacity: Optional[int] = None

class Team(Document):
    sport: str
    team_id: int
    name: str
    abbreviation: str
    city: str
    conference: Optional[str] = None
    division: Optional[str] = None
    founded: Optional[int] = None
    stadium: Optional[Stadium] = None

    class Settings:
        name = "teams"

