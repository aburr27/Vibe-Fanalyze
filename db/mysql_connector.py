import pymysql
from backend.config import settings

def get_mysql_connection():
    return pymysql.connect(
        host=settings.MYSQL_URL,
        user='root',
        password='your_password',
        db='sportsbot'
    )
