import requests
import time
import argparse
import logging
import os
from logging.handlers import TimedRotatingFileHandler

def make_api_request():
    # Define the API endpoint URL
    api_url = "https://example.com/api"  # Replace with your API URL
    
    try:
        # Make the GET request
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            logger.info("API request successful.")
        else:
            logger.warning(f"API request failed with status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make periodic API requests")
    parser.add_argument("--interval", type=int, default=60, help="Time interval between requests in seconds")
    parser.add_argument("--logdir", type=str, default="./logs", help="Directory for log files")
    args = parser.parse_args()

    # Create the log directory if it doesn't exist
    os.makedirs(args.logdir, exist_ok=True)

    # Configure logging to use a TimedRotatingFileHandler for log files
    log_file = os.path.join(args.logdir, "api_requests.log")
    file_handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=30)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    # Create a console handler for logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(logging.INFO)

    while True:
        make_api_request()
        time.sleep(args.interval)
