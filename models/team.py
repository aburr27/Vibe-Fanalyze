from pydantic import BaseModel

class Team(BaseModel):
    id: int
    name: str
    city: str
    league: str
