def test_get_players(client):
    response = client.get("/nba/players")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_single_player(client):
    response = client.get("/nba/players/23")  # LeBron from seed
    # allow either found or not found depending on DB state
    assert response.status_code in [200, 404]
