# app/core/app_factory.py
import importlib
import pkgutil
from fastapi import FastAPI
from app.core.exceptions import AppException, app_exception_handler
from app.core.logging import setup_logging
from app.db.mongo_connector import init_db as init_mongo
from app.db.mysql_connector import get_mysql_connection

logger = setup_logging()


def include_routers(app: FastAPI):
    """Dynamically include all routers from app/routes/*"""
    package = "app.routes"

    for _, sport_name, is_pkg in pkgutil.iter_modules([package.replace(".", "/")]):
        if is_pkg:
            sport_package = f"{package}.{sport_name}"
            for _, module_name, _ in pkgutil.iter_modules([f"{package.replace('.', '/')}/{sport_name}"]):
                module_path = f"{sport_package}.{module_name}"
                module = importlib.import_module(module_path)
                if hasattr(module, "router"):
                    app.include_router(module.router)
                    logger.info(f"✅ Loaded router: {module_path}")


def create_app() -> FastAPI:
    """Factory function to create and configure the FastAPI app."""
    app = FastAPI(title="Vibe-Fanalyze API", version="1.0.0")

    # Register global exception handler
    app.add_exception_handler(AppException, app_exception_handler)

    # Startup events
    @app.on_event("startup")
    async def startup_event():
        logger.info("🚀 Starting up Vibe-Fanalyze API...")

        # Initialize MongoDB
        await init_mongo()
        logger.info("✅ MongoDB initialized")

        # Validate MySQL connection
        conn = get_mysql_connection()
        conn.close()
        logger.info("✅ MySQL connection successful")

        # Include routers dynamically
        include_routers(app)

    @app.get("/")
    def root():
        return {"status": "ok", "message": "Vibe-Fanalyze API is running 🚀"}

    return app
