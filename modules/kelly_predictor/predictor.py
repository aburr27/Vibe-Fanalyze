"""
Prediction utilities: simple rating-differential logistic model and EV calc.
"""
import numpy as np


def predict_win_probability(team_rating: float, opponent_rating: float, home_field_adv: float = 0.0) -> float:
    """Predict win probability from rating differential using a logistic curve.

    The scale is adjustable by dividing the rating diff by a temperature (default 10).
    Returns a probability between 0 and 1.
    """
    rating_diff = team_rating - opponent_rating + home_field_adv
    # Temperature controls steepness; 10 is a reasonable starting point for ratings on a 0-100 scale.
    prob = 1 / (1 + np.exp(-rating_diff / 10))
    return float(prob)

# app/services/kelly_service.py
from modules.kelly_predictor.src.kelly import calculate_bet

def get_kelly_recommendation(team_a, team_b, odds, prob_model):
    win_prob = prob_model.predict(team_a, team_b)
    bet_size = calculate_bet(win_prob, odds)
    return {"win_prob": win_prob, "bet_size": bet_size}


def expected_value(pred_win_prob: float, decimal_odds: float) -> float:
    """Return EV as a proportion (e.g., 0.06 = +6% expected value)."""
    return (pred_win_prob * decimal_odds) - 1