import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_URL = os.getenv("MYSQL_URL", "localhost")
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
