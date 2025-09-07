# app/repositories/mongo_repo.py
from typing import List, Optional
from beanie import PydanticObjectId

from app.models.team import Team
from app.models.player import Player
from app.models.game import Game
from app.models.stats import PlayerStats
from app.models.fantasy import Fantasy
from app.models.betting import Betting


# -------------------- TEAMS --------------------
class TeamRepository:
    @staticmethod
    async def get_all(sport: str) -> List[Team]:
        return await Team.find(Team.sport == sport.lower()).to_list()

    @staticmethod
    async def get_by_id(team_id: int) -> Optional[Team]:
        return await Team.find_one(Team.team_id == team_id)


# -------------------- PLAYERS --------------------
class PlayerRepository:
    @staticmethod
    async def get_all(sport: str) -> List[Player]:
        return await Player.find(Player.sport == sport.lower()).to_list()

    @staticmethod
    async def get_by_id(player_id: int, sport: str) -> Optional[Player]:
        return await Player.find_one(
            Player.player_id == player_id,
            Player.sport == sport.lower()
        )


# -------------------- GAMES --------------------
class GameRepository:
    @staticmethod
    async def get_all(sport: str) -> List[Game]:
        return await Game.find(Game.sport == sport.lower()).to_list()

    @staticmethod
    async def get_by_id(game_id: int, sport: str) -> Optional[Game]:
        return await Game.find_one(
            Game.game_id == game_id,
            Game.sport == sport.lower()
        )


# -------------------- STATS --------------------
class StatsRepository:
    @staticmethod
    async def get_for_game(sport: str, game_id: int) -> List[PlayerStats]:
        return await PlayerStats.find(
            PlayerStats.sport == sport.lower(),
            PlayerStats.game_id == game_id
        ).to_list()


# -------------------- FANTASY --------------------
class FantasyRepository:
    @staticmethod
    async def get_for_player(player_id: int, sport: str) -> Optional[Fantasy]:
        return await Fantasy.find_one(
            Fantasy.player_id == player_id,
            Fantasy.sport == sport.lower()
        )


# -------------------- BETTING --------------------
class BettingRepository:
    @staticmethod
    async def get_for_game(sport: str, game_id: int) -> List[Betting]:
        return await Betting.find(
            Betting.sport == sport.lower(),
            Betting.game_id == game_id
        ).to_list()
