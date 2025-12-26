from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture
def mock_users():
    return [{"id": 1, "username": "testuser", "email": "test@example.com"}]


def test_read_users(mock_users):
    with patch("app.api.v1.user.get_users", return_value=mock_users):
        response = client.get("v1/users/")
        assert response.status_code == 200
        assert response.json() == mock_users
