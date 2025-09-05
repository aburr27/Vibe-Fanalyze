from beanie import Document
from typing import Optional, Dict

class Player(Document):
    sport: str
    player_id: int
    team_id: int
    name: str
    position: Optional[str] = None
    height: Optional[str] = None
    weight: Optional[int] = None
    birthdate: Optional[str] = None
    college: Optional[str] = None
    stats: Optional[Dict] = None  # nested career/season stats

    class Settings:
        name = "players"
