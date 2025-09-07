# app/repositories/mysql_repo.py
from typing import List, Optional
from app.db.mysql_connector import get_mysql_connection


class MySQLRepository:
    """
    Base MySQL repository with helper methods.
    """

    @staticmethod
    def fetch_all(query: str, params: tuple = ()) -> List[dict]:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    @staticmethod
    def fetch_one(query: str, params: tuple = ()) -> Optional[dict]:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row


# -------------------- TEAMS --------------------
class TeamsRepository(MySQLRepository):
    @staticmethod
    def get_teams(sport: str) -> List[dict]:
        return MySQLRepository.fetch_all("""
            SELECT t.* FROM teams t
            JOIN sports s ON t.sport_id = s.id
            WHERE LOWER(s.name) = %s
        """, (sport.lower(),))

    @staticmethod
    def get_team_by_name(name: str, sport: str) -> Optional[dict]:
        return MySQLRepository.fetch_one("""
            SELECT t.* FROM teams t
            JOIN sports s ON t.sport_id = s.id
            WHERE LOWER(s.name) = %s AND t.name = %s
        """, (sport.lower(), name))


# -------------------- GAMES --------------------
class GamesRepository(MySQLRepository):
    @staticmethod
    def get_games(sport: str) -> List[dict]:
        return MySQLRepository.fetch_all("""
            SELECT g.* FROM games g
            JOIN sports s ON g.sport_id = s.id
            WHERE LOWER(s.name) = %s
        """, (sport.lower(),))

    @staticmethod
    def get_game_by_id(game_id: int, sport: str) -> Optional[dict]:
        return MySQLRepository.fetch_one("""
            SELECT g.* FROM games g
            JOIN sports s ON g.sport_id = s.id
            WHERE LOWER(s.name) = %s AND g.id = %s
        """, (sport.lower(), game_id))
