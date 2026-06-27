import pytest
from unittest.mock import MagicMock, patch


@pytest.fixture
def mock_bedrock_client():
    mock_client = MagicMock()
    with patch("app.services.guardrails.get_bedrock_client", return_value=mock_client):
        yield mock_client
