from fastapi import FastAPI
from app.routes import players, teams, games, stats, fantasy

def create_app() -> FastAPI:
    app = FastAPI(title="Vibe-Fanalyze API")
    app.include_router(players.router, prefix="/players")
    app.include_router(teams.router, prefix="/teams")
    app.include_router(games.router, prefix="/games")
    app.include_router(stats.router, prefix="/stats")
    app.include_router(fantasy.router, prefix="/fantasy")
    return app
