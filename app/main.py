# main.py
from fastapi import FastAPI
from app.routes import fantasy, games, players
from app.db.mongo_connector import init_db
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# app/main.py

# Import routers
from app.routes import stats, teams

# Initialize FastAPI app
app = FastAPI(
    title="Vibe-Fanalyze API",
    version="1.0.0",
    description="🏈🏀⚾ A multi-sport platform for fantasy analysis, player tracking, and game predictions."
)

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/teams/{sport}")
async def get_teams(sport: str):
    from app.models.team import Team
    return await Team.find(Team.sport == sport).to_list()

# Root/health check
@app.get("/", tags=["Health Check"])
def root():
    return {"message": "✅ Vibe-Fanalyze is live!"}

# Register routers
# NFL routes (focus)
app.include_router(stats.router, prefix="/nfl/stats", tags=["NFL Stats"])
app.include_router(players.router, prefix="/nfl/players", tags=["NFL Players"])
app.include_router(teams.router, prefix="/nfl/teams", tags=["NFL Teams"])
app.include_router(games.router, prefix="/nfl/games", tags=["NFL Games"])
app.include_router(fantasy.router, prefix="/nfl/fantasy", tags=["NFL Fantasy"])

# NBA routes (later use)
app.include_router(stats.router, prefix="/nba/stats", tags=["NBA Stats"])
app.include_router(players.router, prefix="/nba/players", tags=["NBA Players"])
app.include_router(teams.router, prefix="/nba/teams", tags=["NBA Teams"])
app.include_router(games.router, prefix="/nba/games", tags=["NBA Games"])
app.include_router(fantasy.router, prefix="/nba/fantasy", tags=["NBA Fantasy"])

# WNBA routes (later)
app.include_router(stats.router, prefix="/wnba/stats", tags=["WNBA Stats"])
app.include_router(players.router, prefix="/wnba/players", tags=["WNBA Players"])
app.include_router(teams.router, prefix="/wnba/teams", tags=["WNBA Teams"])
app.include_router(games.router, prefix="/wnba/games", tags=["WNBA Games"])
app.include_router(fantasy.router, prefix="/wnba/fantasy", tags=["WNBA Fantasy"])

# NHL routes (later)
app.include_router(stats.router, prefix="/nhl/stats", tags=["NHL Stats"])
app.include_router(players.router, prefix="/nhl/players", tags=["NHL Players"])
app.include_router(teams.router, prefix="/nhl/teams", tags=["NHL Teams"])
app.include_router(games.router, prefix="/nhl/games", tags=["NHL Games"])
app.include_router(fantasy.router, prefix="/nhl/fantasy", tags=["NHL Fantasy"])

# MLB routes (later)
app.include_router(stats.router, prefix="/mlb/stats", tags=["MLB Stats"])
app.include_router(players.router, prefix="/mlb/players", tags=["MLB Players"])
app.include_router(teams.router, prefix="/mlb/teams", tags=["MLB Teams"])
app.include_router(games.router, prefix="/mlb/games", tags=["MLB Games"])
app.include_router(fantasy.router, prefix="/mlb/fantasy", tags=["MLB Fantasy"])

# MLS routes (later)
app.include_router(stats.router, prefix="/mls/stats", tags=["MLS Stats"])
app.include_router(players.router, prefix="/mls/players", tags=["MLS Players"])
app.include_router(teams.router, prefix="/mls/teams", tags=["MLS Teams"])
app.include_router(games.router, prefix="/mls/games", tags=["MLS Games"])
app.include_router(fantasy.router, prefix="/mls/fantasy", tags=["MLS Fantasy"])
