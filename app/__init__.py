# app/__init__.py
from fastapi import FastAPI
from .core.app_factory import create_app
from .db.mongo_connector import init_db as init_mongo
import asyncio

# Create FastAPI app
app: FastAPI = create_app()

# Initialize MongoDB (Beanie) on startup
@app.on_event("startup")
async def startup_event():
    await init_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    # Add cleanup logic if needed (close DBs, flush logs, etc.)
    pass
