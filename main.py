from fastapi import FastAPI
from backend.routers import stats, players, teams, games, fantasy  # Make sure this matches your folder structure

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

# Health check or landing route
@app.get("/", tags=["Root"])
def root():
    return {"message": "🎉 Welcome to Vibe-Fanalyze!"}

# Include routers
app.include_router(stats.router)
