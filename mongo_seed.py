from backend.db.mongo_connector import mongo_db

# Sample team
team_doc = {
    "id": 1,
    "name": "Los Angeles Lakers",
    "city": "Los Angeles",
    "league": "NBA"
}

# Sample player
player_doc = {
    "id": 23,
    "name": "LeBron James",
    "team": "Los Angeles Lakers",
    "position": "SF",
    "stats": {
        "points": 27.8,
        "rebounds": 8.2,
        "assists": 7.5,
        "steals": 1.3,
        "blocks": 0.9,
        "turnovers": 3.1
    }
}

# Insert into DB
mongo_db.teams.insert_one(team_doc)
mongo_db.players.insert_one(player_doc)

print("MongoDB seeded successfully.")
