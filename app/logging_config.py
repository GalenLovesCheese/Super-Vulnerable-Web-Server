# app/logging_config.py
import logging
import os
from logging.handlers import RotatingFileHandler

def configure_logger():
    log_dir = "app/logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger("flask_app")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    # File handler
    file_handler = RotatingFileHandler(
        f"{log_dir}/app.log", maxBytes=1000000, backupCount=3
    )
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
