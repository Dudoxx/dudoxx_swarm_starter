import pytest
from unittest.mock import patch, MagicMock
from dudoxx_swarm_starter.api_client import get_openai_client

def test_get_openai_client_success():
    with patch('dudoxx_swarm_starter.api_client.OpenAI') as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        client = get_openai_client()
        
        assert client == mock_client
        mock_openai.assert_called_once()

def test_get_openai_client_failure():
    with patch('dudoxx_swarm_starter.api_client.OpenAI') as mock_openai:
        mock_openai.side_effect = Exception("API Error")
        
        with pytest.raises(Exception) as exc_info:
            get_openai_client()
        
        assert str(exc_info.value) == "API Error"