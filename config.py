import os
import logging

# OpenAI API configuration
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Model configuration
DEFAULT_MODEL = "gpt-4"

# Agent configuration
AGENT_ROLES = {
    "customer_support": "You are a helpful customer support agent. Assist users with their inquiries and problems.",
    "sales": "You are a knowledgeable sales agent. Help users with product information and purchasing decisions."
}

# Logging configuration
LOG_FILE = "logs/dudoxx_swarm_starter.log"
LOG_LEVEL = logging.INFO