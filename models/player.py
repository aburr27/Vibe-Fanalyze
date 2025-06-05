from pydantic import BaseModel, Field
from typing import Optional, Dict
from uuid import UUID

class Player(BaseModel):
    id: Optional[int] = Field(None, description="Unique player ID (for SQL)")
    mongo_id: Optional[str] = Field(None, alias="_id", description="MongoDB document ID")
    name: str
    team: str
    position: str
    stats: Optional[Dict[str, float]] = Field(default_factory=dict)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": 23,
                "name": "LeBron James",
                "team": "Los Angeles Lakers",
                "position": "SF",
                "stats": {
                    "points": 28.7,
                    "rebounds": 7.5,
                    "assists": 6.9
                }
            }
        }
