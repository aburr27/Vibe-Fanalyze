from beanie import Document
from typing import Optional, Dict
from datetime import datetime

class Game(Document):
    sport: str
    game_id: int
    season: int
    week: Optional[int] = None
    date: datetime
    home_team_id: int
    away_team_id: int
    status: str  # scheduled | live | finished
    score: Optional[Dict[str, int]] = None
    betting: Optional[Dict] = None

    class Settings:
        name = "games"
