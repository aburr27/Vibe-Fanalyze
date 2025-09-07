# app/config/dev.py
from .base import Settings

class DevSettings(Settings):
    ENVIRONMENT: str = "development"

dev_settings = DevSettings()
