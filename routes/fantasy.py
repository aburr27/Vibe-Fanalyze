from fastapi import APIRouter, HTTPException
from backend.db.mongo_connector import mongo_db
from backend.fantasy_points import calculate_fantasy_points

router = APIRouter(prefix="/fantasy", tags=["Fantasy"])

@router.get("/player/{player_id}")
def get_fantasy_points(player_id: int):
    player = mongo_db.players.find_one({"id": player_id}, {"_id": 0})
    if not player:
        raise HTTPException(status_code=404, detail="Player not found.")

    league = player.get("league", "NBA")  # Default NBA if not set
    stats = player.get("stats", {})
    points = calculate_fantasy_points(stats, league)
    return {"player_id": player_id, "fantasy_points": points}
    
@router.get("/team/{team_name}")
def get_team_fantasy_points(team_name: str, league: str = "NBA"):
    players = list(mongo_db.players.find({"team": team_name, "league": league}, {"_id": 0}))
    if not players:
        raise HTTPException(status_code=404, detail="No players found for team.")

    total = sum(calculate_fantasy_points(p["stats"], league) for p in players)
    return {
        "team": team_name,
        "league": league,
        "fantasy_points_total": total,
        "players": [{ "name": p["name"], "points": calculate_fantasy_points(p["stats"], league)} for p in players]
    }

@router.get("/game/{game_id}")
def get_game_fantasy_points(game_id: int):
    game = mongo_db.games.find_one({"id": game_id}, {"_id": 0})
    if not game:
        raise HTTPException(status_code=404, detail="Game not found.")

    league = game.get("league", "NBA")
    results = {}

    for team, player_stats_list in game.get("stats", {}).items():
        team_total = 0
        results[team] = []

        for stats in player_stats_list:
            points = calculate_fantasy_points(stats, league)
            team_total += points
            results[team].append({
                "player_id": stats.get("id"),
                "points": points
            })

        results[team].append({"team_total_points": team_total})

    return {"game_id": game_id, "league": league, "fantasy_summary": results}
