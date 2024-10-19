import pytest
from unittest.mock import patch, MagicMock
from dudoxx_swarm_starter.main import main

@pytest.fixture
def mock_get_agent():
    with patch('dudoxx_swarm_starter.main.get_agent') as mock:
        yield mock

@pytest.fixture
def mock_input():
    with patch('builtins.input') as mock:
        yield mock

@pytest.fixture
def mock_print():
    with patch('builtins.print') as mock:
        yield mock

def test_main_exit(mock_get_agent, mock_input, mock_print):
    mock_agent = MagicMock()
    mock_get_agent.return_value = mock_agent
    mock_input.side_effect = ["exit"]

    main()

    mock_print.assert_any_call("Welcome to the Dudoxx Swarm Starter!")
    mock_print.assert_any_call("Thank you for using Dudoxx Swarm Starter. Goodbye!")

def test_main_switch_agent(mock_get_agent, mock_input, mock_print):
    mock_agent1 = MagicMock()
    mock_agent2 = MagicMock()
    mock_get_agent.side_effect = [mock_agent1, mock_agent2]
    mock_input.side_effect = ["switch", "sales", "exit"]

    main()

    assert mock_get_agent.call_count == 2
    mock_print.assert_any_call("Switched to sales agent.")

def test_main_process_message(mock_get_agent, mock_input, mock_print):
    mock_agent = MagicMock()
    mock_agent.role = "customer_support"
    mock_agent.process_message.return_value = "Agent response"
    mock_get_agent.return_value = mock_agent
    mock_input.side_effect = ["Hello", "exit"]

    main()

    mock_agent.process_message.assert_called_once_with("Hello")
    mock_print.assert_any_call("[customer_support] Agent: Agent response")

def test_main_error_handling(mock_get_agent, mock_input, mock_print):
    mock_agent = MagicMock()
    mock_agent.process_message.side_effect = Exception("Test error")
    mock_get_agent.return_value = mock_agent
    mock_input.side_effect = ["Hello", "exit"]

    main()

    mock_print.assert_any_call("An error occurred. Please try again.")