import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load variables from .env
load_dotenv()

# MySQL Settings
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_DB = os.getenv("MYSQL_DB", "vibe_fanalyze")

# Properly encode password in case it has special characters
MYSQL_PASSWORD_ENCODED = quote_plus(MYSQL_PASSWORD)

# SQLAlchemy-compatible URL
MYSQL_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD_ENCODED}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

# MongoDB Settings
MONGO_URL = os.getenv("MONGO_URI", "mongodb://localhost:27017/")


