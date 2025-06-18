from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch, MagicMock

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


@patch("requests.post")
def test_get_random_quote_failure_case(mock_post):
    # Create separate mock responses for each API call
    gemini_response = MagicMock()
    gemini_response.status_code = 200
    gemini_response.json.return_value = {
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
    }

    # Second API call (Mailtrap) returns success=False
    mailtrap_response = MagicMock()
    mailtrap_response.status_code = 400
    mailtrap_response.json.return_value = {
        "success": False,
        "errors": ["Invalid email"],
    }

    # Use side_effect to return different responses for each call
    mock_post.side_effect = [gemini_response, mailtrap_response]

    response = client.get(
        "/send-to-email", params={"email": "test@gmail.com", "name": "test"}
    )
    print(response.content)
    assert response.status_code == 400
