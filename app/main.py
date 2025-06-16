from fastapi import FastAPI
from backend.routes import stats, players, teams, games, fantasy  # Make sure this matches your folder structure

@app.get("/")
def root():
    return {"message": "Welcome to Vibe-Fanalyze SportsBot!"}

# Create FastAPI instance
app = FastAPI(
    title="Vibe-Fanalyze API",
    version="1.0.0",
    description="An API for fantasy sports insights, stats, and game predictions across NFL, NBA, MLB, WNBA, UFC, NHL, and MLS."
)

app.include_router(stats.router)
app.include_router(players.router)
app.include_router(teams.router)
app.include_router(games.router)  # new
app.include_router(fantasy.router)

# Health check or landing route
@app.get("/", tags=["Root"])
def root():
    return {"message": "🎉 Welcome to Vibe-Fanalyze!"}

# Include routers
app.include_router(stats.router)

from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Local imports
from backend.routers import stats  # Make sure this matches your folder structure

# Initialize FastAPI app
app = FastAPI(
    title="Vibe-Fanalyze",
    version="1.0.0",
    description="🏈🏀⚾ A multi-sport platform for fantasy analysis, player tracking, and game predictions.",
)

# Root route
@app.get("/", tags=["Health Check"])
def root():
    return {"message": "✅ Vibe-Fanalyze is live!"}

# Register routers
app.include_router(stats.router)

