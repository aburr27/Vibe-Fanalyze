"""
Prediction Service
------------------
Handles simple matchup predictions for Vibe-Fanalyze.
Can be upgraded later with your machine learning or API model.
"""

import random

def get_game_prediction(team_a: str, team_b: str) -> dict:
    """
    Mock prediction logic (replace with your model)
    Returns: {favorite, underdog, probability}
    """
    prob_a = round(random.uniform(0.4, 0.65), 2)
    prob_b = round(1 - prob_a, 2)
    favorite = team_a if prob_a > prob_b else team_b
    underdog = team_b if prob_a > prob_b else team_a

    return {
        "team_a": team_a,
        "team_b": team_b,
        "probability": prob_a if prob_a > prob_b else prob_b,
        "favorite": favorite,
        "underdog": underdog
    }
