from app.repositories.mongo_repo import MongoRepo

class BettingRepo:
    def __init__(self):
        self.mongo = MongoRepo()

    def get_betting_for_game(self, sport: str, game_id: int) -> dict | None:
        return self.mongo.find_one('betting', {'sport': sport.upper(), 'game_id': game_id})
