from pydantic import BaseModel, Field
from pydantic import BaseModel
from pydantic import BaseModel
from typing import Optional

class Team(BaseModel):
    id: Optional[int] = Field(None, description="Unique team ID (for SQL)")
    mongo_id: Optional[str] = Field(None, alias="_id", description="MongoDB document ID")
    name: str
    city: str
    league: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Warriors",
                "city": "San Francisco",
                "league": "NBA"
            }
        }