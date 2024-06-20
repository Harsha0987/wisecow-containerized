import requests
import logging
import time

# Set up logging
logging.basicConfig(filename='application_health.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Configuration
URL = 'https://github.com/Harsha0987/wisecow-containerized'
CHECK_INTERVAL = 60  

def check_application_health(url):
    try:
        response = requests.get(url)
        if 200 <= response.status_code < 300:
            logging.info(f'Application is UP. Status Code: {response.status_code}')
            print(f'Application is UP. Status Code: {response.status_code}')
        else:
            logging.warning(f'Application is DOWN. Status Code: {response.status_code}')
            print(f'Application is DOWN. Status Code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        logging.error(f'Failed to reach the application. Error: {str(e)}')
        print(f'Failed to reach the application. Error: {str(e)}')

def monitor_application(url, interval):
    while True:
        check_application_health(url)
        time.sleep(interval)

if __name__ == "__main__":
    monitor_application(URL, CHECK_INTERVAL)
