@router.post("/kelly/predict")
def kelly_predict(data: KellyInput):
    return get_kelly_recommendation(data.team_a, data.team_b, data.odds, model)
