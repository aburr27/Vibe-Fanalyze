"""
Kelly Criterion Betting Service
--------------------------------
Handles bankroll optimization and expected value calculations for Vibe-Fanalyze.
"""

import math

def calculate_kelly_fraction(win_prob: float, odds: float) -> float:
    """
    Calculate Kelly fraction for a single bet.
    win_prob: model's predicted probability (0.0–1.0)
    odds: decimal odds from sportsbook (e.g., 1.85)
    """
    b = odds - 1
    q = 1 - win_prob
    kelly_fraction = ((b * win_prob) - q) / b if b != 0 else 0
    return max(kelly_fraction, 0)  # never negative


def get_kelly_recommendation(team_a: str, team_b: str, odds: dict, model=None):
    """
    Returns optimal bet sizing recommendation for the given matchup.
    odds = {"team_a": 1.85, "team_b": 2.10}
    """

    # --- Mock prediction model (replace with ML model later) ---
    win_prob_a = 0.58  # Example: from prediction_service
    win_prob_b = 1 - win_prob_a

    kelly_a = calculate_kelly_fraction(win_prob_a, odds["team_a"])
    kelly_b = calculate_kelly_fraction(win_prob_b, odds["team_b"])

    recommended_team = team_a if kelly_a > kelly_b else team_b
    recommended_size = max(kelly_a, kelly_b)

    return {
        "team_a": team_a,
        "team_b": team_b,
        "win_prob_a": win_prob_a,
        "win_prob_b": win_prob_b,
        "kelly_a": kelly_a,
        "kelly_b": kelly_b,
        "recommended_team": recommended_team,
        "bet_size": round(recommended_size, 3)
    }
