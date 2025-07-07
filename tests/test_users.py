def test_create_user(client):
    payload = {"name": "Test User", "email": "testuser@example.com"}
    response = client.post("/users/", json=payload)
    assert response.status_code in (200, 201), response.text
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert "id" in data

def test_create_user_validation_error(client):
    response = client.post("/users/", json={"email": "not-an-email"})
    assert response.status_code == 422

def test_get_users(client):
    # Should at least return the one user we created above
    response = client.get("/users/")
    assert response.status_code == 200, response.text
    users = response.json()
    assert isinstance(users, list)
    assert any(u["email"] == "testuser@example.com" for u in users)
