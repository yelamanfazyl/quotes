from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch

client = TestClient(app)


@patch("random.choice")
def test_get_random_quote(mock_choice):
    mock_choice.return_value = "test quote"
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["quote"] == "test quote"
