# app/db/mongo_connector.py
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
# from app.db.mongo_connector import init_db, client

# Import Beanie document models
from app.models.team import Team
from app.models.player import Player
from app.models.game import Game
from app.models.stats import PlayerStats
from app.models.fantasy import Fantasy
from app.models.betting import Betting

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "vibe_fanalyze"

# Async MongoDB client
client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]

async def init_db():
    """
    Initialize Beanie with all document models.
    Call this once at application startup.
    """
    await init_beanie(
        database=db,
        document_models=[Team, Player, Game, PlayerStats, Fantasy, Betting]
    )

# Helper to run initialization (optional)
def run_init():
    asyncio.run(init_db())


async def main():
    await init_db()
    print(await client['vibe_fanalyze']['games'].find_one({}))

if __name__ == "__main__":
    asyncio.run(main())
