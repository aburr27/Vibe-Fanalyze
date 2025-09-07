from beanie import Document
from typing import Optional, Dict

class PlayerStats(Document):
    sport: str
    game_id: int
    mysql_game_id: Optional[int] = None
    player_id: int
    mysql_player_id: Optional[int] = None
    team_id: int
    mysql_team_id: Optional[int] = None
    season: int
    week: Optional[int] = None
    stats: Dict = {}

    class Settings:
        name = "stats"

