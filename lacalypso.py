import requests
import time
import argparse
import logging

def make_api_request():

    api_url = " https://kuma.flotech.be/api/push/DqF1v25TRr?status=up&msg=OK&ping="  # Replace with your API URL
    
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
    parser.add_argument("--logfile", type=str, default="api_requests.log", help="Path to the log file")
    args = parser.parse_args()

    # Configure logging to write to the specified log file
    logging.basicConfig(filename=args.logfile, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger()

    while True:
        make_api_request()
        time.sleep(args.interval)
