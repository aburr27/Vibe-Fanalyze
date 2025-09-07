from app.repositories.mysql_repo import MySQLRepo
from app.repositories.mongo_repo import MongoRepo

class GamesRepo:
    def __init__(self):
        self.mysql = MySQLRepo()
        self.mongo = MongoRepo()

    def list_games_by_sport(self, sport: str) -> list[dict]:
        query = """
            SELECT g.*, s.name as sport_name
            FROM games g
            JOIN sports s ON g.sport_id = s.id
            WHERE LOWER(s.name) = %s
        """
        return self.mysql.fetch_all(query, (sport.lower(),))

    def get_game_by_id(self, game_id: int) -> dict | None:
        query = "SELECT * FROM games WHERE id = %s"
        return self.mysql.fetch_one(query, (game_id,))
