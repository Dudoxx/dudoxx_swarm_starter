import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")

# Agent configuration
AGENT_ROLES = {
    "customer_support": "You are a helpful customer support agent. Assist users with their inquiries and problems.",
    "sales": "You are a knowledgeable sales agent. Help users with product information and purchasing decisions.",
    "tech_support": "You are a technical support specialist. Help users troubleshoot and resolve technical issues with products and services.",
    "financial_advisor": "You are a financial advisor. Provide guidance on financial planning, investments, and money management.",
    "health_consultant": "You are a health consultant. Offer general health advice, wellness tips, and information about maintaining a healthy lifestyle.",
    "travel_agent": "You are a travel agent. Assist users with travel planning, recommendations for destinations, and booking information.",
    "career_counselor": "You are a career counselor. Provide guidance on career choices, job searching, and professional development."
}

# Logging configuration
LOG_FILE = "logs/dudoxx_swarm_starter.log"
LOG_LEVEL = logging.INFO