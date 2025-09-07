from app.repositories.mongo_repo import MongoRepo

class StatsRepo:
    def __init__(self):
        self.mongo = MongoRepo()

    def list_stats_by_sport(self, sport: str) -> list[dict]:
        return self.mongo.find_many('analytics', {'league': sport.upper()})

    def get_player_stats(self, player_id: int) -> dict | None:
        return self.mongo.find_one('analytics', {'entityId': player_id})
