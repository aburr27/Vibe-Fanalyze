from beanie import Document
from typing import Dict
from datetime import datetime

class Betting(Document):
    sport: str              # "NFL", "NBA", etc.
    game_id: int            # links to Game
    sportsbook: str         # "DraftKings", "FanDuel", etc.
    market: str             # "moneyline", "spread", "over_under", "total"
    line: Dict              # odds structure (varies by market type)
    timestamp: datetime     # last update time

    class Settings:
        name = "betting"
