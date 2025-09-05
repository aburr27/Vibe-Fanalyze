from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql
from app.config.settings import settings

# SQLAlchemy engine
engine = create_engine(settings.MYSQL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Raw PyMySQL connection
def get_mysql_connection():
    return pymysql.connect(
        host=settings.MYSQL_HOST,
        user=settings.MYSQL_USER,
        password=settings.MYSQL_PASSWORD,
        database=settings.MYSQL_DB,
        port=int(settings.MYSQL_PORT),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
