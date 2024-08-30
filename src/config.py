# config.py

import logging
import os

# Set up logging directory
log_dir = "../logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(f"{log_dir}/logging.log", mode='a'),
                        logging.StreamHandler()
                    ])

def get_logger(name):
    """
    Returns a logger with the given name, with the predefined logging configuration.
    """
    return logging.getLogger(name)
