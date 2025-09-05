from .base import Settings

class ProdSettings(Settings):
environment: str = "production"

prod_settings = ProdSettings()