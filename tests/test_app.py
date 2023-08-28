from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

def test_app():
    response = client.get('/static')
    assert response.status_code == 200
    assert "Essa página é estática" in response.text
