# app/config/prod.py
from .base import Settings

class ProdSettings(Settings):
    ENVIRONMENT: str = "production"

prod_settings = ProdSettings()
