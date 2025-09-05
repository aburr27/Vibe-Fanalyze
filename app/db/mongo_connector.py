# app/db/mongo_connector.py
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.betting import Betting
import asyncio

# Import models
from app.models.team import Team
from app.models.player import Player
from app.models.game import Game
from app.models.stats import PlayerStats
from app.models.fantasy import Fantasy
from app.models.betting import Betting  # NEW ✅

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "vibe_fanalyze"

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]

async def init_db():
    await init_beanie(
        database=db,
        document_models=[Team, Player, Game, PlayerStats, Fantasy, Betting]
    )
