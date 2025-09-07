from app.repositories.mysql_repo import MySQLRepo
from app.repositories.mongo_repo import MongoRepo

class PlayersRepo:
    def __init__(self):
        self.mysql = MySQLRepo()
        self.mongo = MongoRepo()

    def list_players_by_sport(self, sport: str) -> list[dict]:
        query = """
            SELECT p.*, t.sport_id
            FROM players p
            JOIN teams t ON p.team_id = t.id
            JOIN sports s ON t.sport_id = s.id
            WHERE LOWER(s.name) = %s
        """
        return self.mysql.fetch_all(query, (sport.lower(),))

    def get_player_by_id(self, player_id: int) -> dict | None:
        query = "SELECT * FROM players WHERE id = %s"
        return self.mysql.fetch_one(query, (player_id,))
