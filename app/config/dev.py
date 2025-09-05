from .base import Settings

class DevSettings(Settings):
environment: str = "development"

dev_settings = DevSettings()