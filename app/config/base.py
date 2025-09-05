from pydantic import BaseSettings

class Settings(BaseSettings):
app_name: str = "Vibe-Fanalyze"
environment: str = "development"
mysql_url: str = "mysql://user:password@localhost:3306/vibe_fanalyze"
mongodb_url: str = "mongodb://localhost:27017"

class Config:
env_file = ".env"

settings = Settings()