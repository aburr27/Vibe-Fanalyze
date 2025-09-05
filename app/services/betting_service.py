from typing import Dict

# Mock NFL betting data per game
nfl_betting = {
    1: {  # game_id
        "moneyline": {"Cowboys": -150, "Eagles": +130},
        "spread": {"Cowboys": -3.5, "Eagles": +3.5},
        "total": {"over": 45.5, "under": 45.5}
    },
    2: {
        "moneyline": {"Chiefs": -200, "Packers": +170},
        "spread": {"Chiefs": -7.0, "Packers": +7.0},
        "total": {"over": 50.0, "under": 50.0}
    }
}

# Mock NBA betting data per game
nba_betting = {
    101: {
        "moneyline": {"Lakers": -120, "Celtics": +110},
        "spread": {"Lakers": -2.5, "Celtics": +2.5},
        "total": {"over": 220.5, "under": 220.5}
    },
    102: {
        "moneyline": {"Warriors": -150, "Bulls": +130},
        "spread": {"Warriors": -4.0, "Bulls": +4.0},
        "total": {"over": 225.0, "under": 225.0}
    }
}

def get_betting(sport: str, game_id: int) -> Dict:
    """
    Returns betting info for a given sport and game_id.
    """
    sport = sport.lower()
    if sport == "nfl":
        return nfl_betting.get(game_id, {"error": "No betting data for this game"})
    elif sport == "nba":
        return nba_betting.get(game_id, {"error": "No betting data for this game"})
    return {"error": "Sport not supported"}
