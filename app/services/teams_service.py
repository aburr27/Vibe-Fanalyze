from app.db.mysql_connector import mysql_conn
from app.models.teams import Team

def get_teams(sport: str):
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT teams.* FROM teams
        JOIN sports ON teams.sport_id = sports.id
        WHERE LOWER(sports.name) = %s
    """, (sport.lower(),))
    rows = cursor.fetchall()
    cursor.close()
    return [Team(**row).dict() for row in rows]

def get_team_by_name(name: str, sport: str):
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT teams.* FROM teams
        JOIN sports ON teams.sport_id = sports.id
        WHERE LOWER(sports.name) = %s AND teams.name = %s
    """, (sport.lower(), name))
    row = cursor.fetchone()
    cursor.close()
    if row:
        return Team(**row).dict()
    return None
