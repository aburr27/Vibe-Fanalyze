# scripts/mongo_seed.py
import asyncio
from app.db.mongo_connector import db, init_db


async def seed_mongo():
    # Ensure Beanie models are initialized
    await init_db()

    # Drop old collections for a clean slate
    await db.leagues.drop()
    await db.teams.drop()
    await db.players.drop()
    await db.chat_logs.drop()

    # Seed chat logs
    await db.chat_logs.insert_one({"user_id": "seed_user", "message": "Hello World!"})

    # Leagues
    leagues = [
        {"code": "NFL", "name": "National Football League"},
        {"code": "NBA", "name": "National Basketball Association"},
        {"code": "MLB", "name": "Major League Baseball"},
        {"code": "WNBA", "name": "Women's National Basketball Association"},
        {"code": "UFC", "name": "Ultimate Fighting Championship"},
        {"code": "NHL", "name": "National Hockey League"},
        {"code": "MLS", "name": "Major League Soccer"},
    ]

    # Teams
    teams = [
        {"id": 1, "name": "Los Angeles Lakers", "city": "Los Angeles", "league": "NBA"},
        {"id": 2, "name": "Dallas Cowboys", "city": "Dallas", "league": "NFL"},
        {"id": 3, "name": "New York Yankees", "city": "New York", "league": "MLB"},
        {"id": 4, "name": "Las Vegas Aces", "city": "Las Vegas", "league": "WNBA"},
        {"id": 5, "name": "Jon Jones", "city": "Albuquerque", "league": "UFC"},
        {"id": 6, "name": "Toronto Maple Leafs", "city": "Toronto", "league": "NHL"},
        {"id": 7, "name": "LA Galaxy", "city": "Los Angeles", "league": "MLS"},
    ]

    # Players
    players = [
        {
            "id": 23,
            "name": "LeBron James",
            "team": "Los Angeles Lakers",
            "position": "SF",
            "stats": {"points": 27.2, "assists": 7.4, "rebounds": 7.6},
        },
        {
            "id": 4,
            "name": "Dak Prescott",
            "team": "Dallas Cowboys",
            "position": "QB",
            "stats": {"passing_yards": 3800, "tds": 30, "ints": 9},
        },
        {
            "id": 99,
            "name": "Aaron Judge",
            "team": "New York Yankees",
            "position": "OF",
            "stats": {"home_runs": 52, "avg": 0.287},
        },
    ]

    # Insert new data
    await db.leagues.insert_many(leagues)
    await db.teams.insert_many(teams)
    await db.players.insert_many(players)

    print("✅ MongoDB seeded with leagues, teams, and players.")


if __name__ == "__main__":
    asyncio.run(seed_mongo())
