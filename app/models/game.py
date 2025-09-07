from beanie import Document
from typing import Optional, Dict
from datetime import datetime

class Game(Document):
    sport: str
    game_id: int
    mysql_game_id: Optional[int] = None  # cross-reference to MySQL games table
    season: int
    week: Optional[int] = None
    date: datetime
    home_team_id: int
    away_team_id: int
    status: str = "scheduled"  # scheduled | live | finished
    score: Optional[Dict[str, int]] = {}
    betting: Optional[Dict] = {}

    class Settings:
        name = "games"

