"""
This module is used for logging purpose.
"""

import os
import sys
import logging

LOGGING_STRING = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

LOG_DIR = "logs"
log_filepath = os.path.join(LOG_DIR, "running_logs.log")
os.makedirs(LOG_DIR, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=LOGGING_STRING,
    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)],
)
