# app/config/base.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Vibe-Fanalyze"
    ENVIRONMENT: str = "development"

    # MySQL Config
    MYSQL_USER: str = "user"
    MYSQL_PASSWORD: str = "password"
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_DB: str = "vibe_fanalyze"

    # MongoDB Config
    MONGO_URL: str = "mongodb://localhost:27017"
    MONGO_DB: str = "vibe_fanalyze"

    class Config:
        env_file = ".env"
        case_sensitive = True

    @property
    def MYSQL_URL(self) -> str:
        return (
            f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
        )

# Default settings (can be overridden by dev/prod)
settings = Settings()
