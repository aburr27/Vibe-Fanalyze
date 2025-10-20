"""
VibeBot: Intelligent Sports Analytics Assistant for Vibe-Fanalyze

- Provides chat-style interaction via API or UI
- Can retrieve stats, generate predictions, and calculate optimal bet sizes
- Integrates with Kelly Criterion module and predictive models
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.kelly_service import get_kelly_recommendation
from app.services.prediction_service import get_game_prediction
from app.services.db_mongo import save_chat_log
from app.services.db_mysql import save_prediction_log
from fastapi import APIRouter, HTTPException


router = APIRouter()

# ----------- Data Models -----------

class VibeBotRequest(BaseModel):
    user_query: str
    team_a: str | None = None
    team_b: str | None = None
    odds: dict | None = None  # Example: {"team_a": 1.85, "team_b": 2.10}


class VibeBotResponse(BaseModel):
    response: str
    data: dict | None = None

# ----------- Core Logic -----------

@router.post("/vibebot", response_model=VibeBotResponse)
async def vibebot_chat(request: VibeBotRequest):
    """
    Chat interface for Vibe-Fanalyze AI assistant.
    Understands basic sports-related intents:
    - prediction requests
    - betting / Kelly analysis
    - general greetings
    """

    query = request.user_query.lower()

    try:
        # Greeting intent
        if "hello" in query or "hi" in query or "hey" in query:
            return VibeBotResponse(response="Hey there! I’m VibeBot 🤖 — your sports analytics assistant. What matchup do you want to analyze today?")

        # Prediction intent
        elif "predict" in query or "who will win" in query:
            if not (request.team_a and request.team_b):
                raise HTTPException(status_code=400, detail="Please include 'team_a' and 'team_b' in your request.")
            
            prediction = get_game_prediction(request.team_a, request.team_b)
            return VibeBotResponse(
                response=f"I predict {prediction['favorite']} has a {prediction['probability']*100:.1f}% chance to win over {prediction['underdog']}.",
                data=prediction
            )

        # Kelly criterion / betting intent
        elif "bet" in query or "kelly" in query or "odds" in query:
            if not (request.team_a and request.team_b and request.odds):
                raise HTTPException(status_code=400, detail="Please include 'team_a', 'team_b', and 'odds' in your request.")

            kelly = get_kelly_recommendation(request.team_a, request.team_b, request.odds, model=None)
            return VibeBotResponse(
                response=f"Using the Kelly Criterion, your optimal bet size is {kelly['bet_size']*100:.2f}% of your bankroll.",
                data=kelly
            )
try:
        if "predict" in query or "who will win" in query:
            prediction = get_game_prediction(request.team_a, request.team_b)
            save_prediction_log(prediction)
            await save_chat_log(request.user_query, f"I predict {prediction['favorite']} has a {prediction['probability']*100:.1f}% chance.", prediction)
            return VibeBotResponse(
                response=f"I predict {prediction['favorite']} has a {prediction['probability']*100:.1f}% chance to win over {prediction['underdog']}.",
                data=prediction
            )

        elif "bet" in query or "kelly" in query:
            kelly = get_kelly_recommendation(request.team_a, request.team_b, request.odds, model=None)
            save_prediction_log(kelly)
            await save_chat_log(request.user_query, f"Optimal bet: {kelly['bet_size']*100:.2f}% on {kelly['recommended_team']}", kelly)
            return VibeBotResponse(
                response=f"Using Kelly, your optimal bet is {kelly['bet_size']*100:.2f}% on {kelly['recommended_team']}.",
                data=kelly
            )

        else:
            await save_chat_log(request.user_query, "Try asking for a prediction or Kelly analysis.")
            return VibeBotResponse(response="I didn’t catch that — try asking about a matchup or odds.")

        # Default fallback
        else:
            return VibeBotResponse(response="I didn’t quite catch that. Try asking for a game prediction or Kelly bet suggestion!")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
