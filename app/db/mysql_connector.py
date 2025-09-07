# app/db/mysql_connector.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql
from app.config.settings import settings
# from app.db.mysql_connector import get_mysql_connection

# SQLAlchemy engine for ORM queries
engine = create_engine(settings.MYSQL_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Raw PyMySQL connection for direct SQL queries
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
# Example usage (remove or move to a test script before production):
# conn = get_mysql_connection()
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM users LIMIT 1")
# print(cursor.fetchone())
# conn.close()
