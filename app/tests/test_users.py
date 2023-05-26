from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_users():
    response = client.get("/v1/users/")
    assert response.status_code == 200
    assert response.json()
