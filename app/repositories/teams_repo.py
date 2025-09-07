from app.repositories.mysql_repo import MySQLRepo
from app.repositories.mongo_repo import MongoRepo

class TeamsRepo:
    def __init__(self):
        self.mysql = MySQLRepo()
        self.mongo = MongoRepo()

    def list_teams_by_sport(self, sport: str) -> list[dict]:
        query = """
            SELECT t.*, s.name as sport_name
            FROM teams t
            JOIN sports s ON t.sport_id = s.id
            WHERE LOWER(s.name) = %s
        """
        return self.mysql.fetch_all(query, (sport.lower(),))

    def get_team_by_name(self, name: str, sport: str) -> dict | None:
        query = """
            SELECT t.*, s.name as sport_name
            FROM teams t
            JOIN sports s ON t.sport_id = s.id
            WHERE LOWER(s.name) = %s AND t.name = %s
        """
        return self.mysql.fetch_one(query, (sport.lower(), name))
