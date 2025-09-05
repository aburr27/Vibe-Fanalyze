from beanie import Document
from typing import Optional, Dict

class PlayerStats(Document):
    sport: str
    game_id: int
    player_id: int
    team_id: int
    season: int
    week: Optional[int] = None
    stats: Dict  # nested per category (passing, rushing, etc.)

    class Settings:
        name = "stats"
