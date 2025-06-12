from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch, MagicMock, PropertyMock
from requests import Response
import mock

client = TestClient(app)


@patch("requests.post")
def test_get_random_quote(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.side_effect = [
        {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {
                                "text": '"Debugging: Where the real fun begins... said no programmer ever."'
                            }
                        ],
                    },
                }
            ],
        },
        {"success": True, "message_ids": ["0c7fd939-02cf-11ed-88c2-0a58a9feac02"]},
    ]
    response = client.get(
        "/send-to-email", params={"email": "test@gmail.com", "name": "test"}
    )
    assert response.status_code == 200


@patch("requests.models.Response.status_code")
@patch("requests.post")
def test_get_random_quote_other_test(mock_post, status_code):
    status_code = 200
    mock_post.return_value.json.side_effect = [
        {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {
                                "text": '"Debugging: Where the real fun begins... said no programmer ever."'
                            }
                        ],
                    },
                }
            ],
        },
        {"success": True, "message_ids": ["0c7fd939-02cf-11ed-88c2-0a58a9feac02"]},
    ]
    response = client.get(
        "/send-to-email", params={"email": "test@gmail.com", "name": "test"}
    )
    print(response.content)
    assert response.status_code == 500
