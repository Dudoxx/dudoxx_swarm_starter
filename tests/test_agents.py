import pytest
from unittest.mock import patch, MagicMock
from dudoxx_swarm_starter.agents import Agent, get_agent
from dudoxx_swarm_starter.config import AGENT_ROLES

@pytest.fixture
def mock_client():
    with patch('dudoxx_swarm_starter.agents.client') as mock:
        yield mock

def test_agent_initialization():
    agent = Agent("customer_support")
    assert agent.role == "customer_support"
    assert agent.instructions == AGENT_ROLES["customer_support"]

def test_agent_process_message(mock_client):
    agent = Agent("sales")
    mock_client.chat.completions.create.return_value.choices[0].message.content = "Test response"
    
    response = agent.process_message("Test input")
    
    assert response == "Test response"
    mock_client.chat.completions.create.assert_called_once()

def test_agent_process_message_error(mock_client):
    agent = Agent("customer_support")
    mock_client.chat.completions.create.side_effect = Exception("API Error")
    
    response = agent.process_message("Test input")
    
    assert "An error occurred" in response

def test_get_agent_valid_role():
    agent = get_agent("sales")
    assert isinstance(agent, Agent)
    assert agent.role == "sales"

def test_get_agent_invalid_role():
    with pytest.raises(ValueError) as exc_info:
        get_agent("invalid_role")
    
    assert "Unknown agent role" in str(exc_info.value)