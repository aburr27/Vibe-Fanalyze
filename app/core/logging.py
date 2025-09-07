# app/core/logging.py
import logging


def setup_logging():
    """Configure and return the main application logger."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logger = logging.getLogger("vibe-fanalyze")
    return logger
