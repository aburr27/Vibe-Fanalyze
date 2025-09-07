from app.repositories.mongo_repo import MongoRepo

class FantasyRepo:
    def __init__(self):
        self.mongo = MongoRepo()

    def list_fantasy_by_sport(self, sport: str) -> list[dict]:
        return self.mongo.find_many('fantasy', {'sport': sport.upper()})

    def get_fantasy_by_player(self, player_id: int) -> dict | None:
        return self.mongo.find_one('fantasy', {'player_id': player_id})
