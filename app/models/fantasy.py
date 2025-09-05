from beanie import Document
from typing import Optional, Dict

class Fantasy(Document):
    sport: str
    player_id: int
    season: int
    week: Optional[int] = None
    fantasy_points: float
    projections: Optional[Dict] = None
    scoring_rules: Optional[Dict] = None

    class Settings:
        name = "fantasy"
