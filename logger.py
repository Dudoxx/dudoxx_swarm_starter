import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(log_file, log_level=logging.INFO):
    logger = logging.getLogger('dudoxx_swarm_starter')
    logger.setLevel(log_level)

    # Create logs directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create file handler which logs even debug messages
    file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
    file_handler.setLevel(log_level)

    # Create console handler with a higher log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger