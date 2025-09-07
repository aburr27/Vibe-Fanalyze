from beanie import Document
from typing import Optional, Dict

class Fantasy(Document):
    sport: str
    player_id: int
    mysql_player_id: Optional[int] = None  # cross-reference to MySQL players table
    season: int
    week: Optional[int] = None
    fantasy_points: float = 0.0
    projections: Optional[Dict] = {}
    scoring_rules: Optional[Dict] = {}

    class Settings:
        name = "fantasy"

