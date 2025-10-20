# main.py
from fastapi import FastAPI
from app.routes import fantasy, games, players 
from app.db.mongo_connector import init_db as init_mongo
from dotenv import load_dotenv
from app import vibebot
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.db.mysql_connector import get_mysql_connection
from app.routes import chat_routes, vibebot
import os
import importlib
import pkgutil

app = FastAPI(title="Vibe-Fanalyze Dashboard")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(chat_routes.router)
app.include_router(vibebot.router)

app = FastAPI(title="Vibe-Fanalyze Analytics Dashboard")

# Include routes
app.include_router(vibebot.router, prefix="/api", tags=["VibeBot"])

# Static and templates setup
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

app = FastAPI(title="Vibe-Fanalyze Sports Analytics")

# Routers
app.include_router(vibebot.router, prefix="/api", tags=["VibeBot"])

# Serve templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

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

# Dynamically include all routers from app/routes/*
def include_routers():
    package = "app.routes"

    # Walk through all sub packages (nba, nfl, mlb, etc.)
    for _, sport_name, is_pkg in pkgutil.iter_modules([package.replace(".", "/")]):
        if is_pkg:
            sport_package = f"{package}.{sport_name}"
            # Scan inside each sport folder (games_routes, players_routes, etc.)
            for _, module_name, _ in pkgutil.iter_modules([f"{package.replace('.', '/')}/{sport_name}"]):
                module_path = f"{sport_package}.{module_name}"
                module = importlib.import_module(module_path)
                if hasattr(module, "router"):
                    app.include_router(module.router)


@app.on_event("startup")
async def startup_event():
    # Init MongoDB (Beanie models)
    await init_mongo()

    # Test MySQL connection (raises if bad config)
    conn = get_mysql_connection()
    conn.close()

    # Register all sport-specific routers
    include_routers()

@app.get("/")
def root():
    return {"status": "ok", "message": "Vibe-Fanalyze API is running 🚀"}

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
