from beanie import Document
from typing import Dict, Optional
from datetime import datetime

class Betting(Document):
    sport: str
    game_id: int                   # Mongo Game document ID or MySQL game_id
    mysql_game_id: Optional[int] = None  # optional MySQL reference
    sportsbook: str
    market: str
    line: Dict = {}
    timestamp: datetime = datetime.utcnow()

    class Settings:
        name = "betting"

