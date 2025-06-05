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
