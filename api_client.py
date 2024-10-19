from openai import OpenAI
from config import OPENAI_API_KEY
from logger import setup_logger
from config import LOG_FILE, LOG_LEVEL

logger = setup_logger(LOG_FILE, LOG_LEVEL)

def get_openai_client():
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        logger.info("OpenAI client initialized successfully")
        return client
    except Exception as e:
        logger.error(f"Error initializing OpenAI client: {e}")
        raise

client = get_openai_client()