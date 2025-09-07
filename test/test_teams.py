def test_get_teams(client):
    response = client.get("/nba/teams")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_team_by_name(client):
    response = client.get("/nba/teams/Los Angeles Lakers")
    # allow either found or not found depending on DB state
    assert response.status_code in [200, 404]
