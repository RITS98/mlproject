import logging
import os
from datetime import datetime

# Create a log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Define the logs directory path
logs_dir = os.path.join(os.getcwd(), 'logs')
# Ensure the logs directory exists
os.makedirs(logs_dir, exist_ok=True)
# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
