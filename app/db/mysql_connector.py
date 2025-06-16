import pymysql
from backend.config import settings

def get_mysql_connection():
    return pymysql.connect(
        host=settings.MYSQL_HOST,
        user=settings.MYSQL_USER,
        password=settings.MYSQL_PASSWORD,
        database=settings.MYSQL_DB,
        port=int(settings.MYSQL_PORT),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
