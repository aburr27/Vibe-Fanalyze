from app.db.mysql_connector import mysql_conn
from app.models.teams import Team

def get_teams(sport: str):
    cursor = mysql_conn.cursor(dictionary=True)
    query = "SELECT * FROM teams WHERE sport=%s"
    cursor.execute(query, (sport.lower(),))
    rows = cursor.fetchall()
    cursor.close()
    return [Team(**row).dict() for row in rows]
