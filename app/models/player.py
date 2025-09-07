from beanie import Document
from typing import Optional, Dict

class Player(Document):
    sport: str
    player_id: int
    mysql_player_id: Optional[int] = None  # MySQL reference
    team_id: int
    mysql_team_id: Optional[int] = None    # MySQL reference
    name: str
    position: Optional[str] = None
    height: Optional[str] = None
    weight: Optional[int] = None
    birthdate: Optional[str] = None
    college: Optional[str] = None
    stats: Optional[Dict] = {}

    class Settings:
        name = "players"

