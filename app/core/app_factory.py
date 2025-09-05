from fastapi import FastAPI

def create_app() -> FastAPI:
#Factory function to create and configure the FastAPI app.
app = FastAPI(title="Vibe-Fanalyze API", version="1.0.0")

# Import and include routes here
from app.routes import health
app.include_router(health.router)


return app