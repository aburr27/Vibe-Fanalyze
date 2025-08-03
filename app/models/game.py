from sqlalchemy import Column, Integer, String, DateTime
from .player import Base

class Game(BaseModel):
    id: int
    home_team: str
    away_team: str
    league: str
    date: datetime
    stats: Optional[Dict] = Field(default_factory=dict)
    result: Optional[str] = None  # e.g. "home_win", "away_win", "draw"


