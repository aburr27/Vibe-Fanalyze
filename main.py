from fastapi import FastAPI
from backend.routers import stats  # Make sure this matches your folder structure

# Create FastAPI instance
app = FastAPI(
    title="Vibe-Fanalyze API",
    version="1.0.0",
    description="An API for fantasy sports insights, stats, and game predictions across NFL, NBA, MLB, WNBA, UFC, NHL, and MLS."
)

# Health check or landing route
@app.get("/", tags=["Root"])
def root():
    return {"message": "🎉 Welcome to Vibe-Fanalyze!"}

# Include routers
app.include_router(stats.router)
