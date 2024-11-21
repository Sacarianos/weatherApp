import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_URL = "https://api.openweathermap.org/data/2.5/"

def fetch_current_weather(zip_code, api_key, units="metric"):
    """Fetch current weather data for a given zip code."""
    try:
        params = {'zip': zip_code, 'appid': api_key, 'units': units}
        response = requests.get(BASE_URL + "weather", params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error occurred: {req_err}")
    return None

def fetch_forecast(zip_code, api_key, units="metric"):
    """Fetch 5-day weather forecast for a given zip code."""
    try:
        params = {'zip': zip_code, 'appid': api_key, 'units': units}
        response = requests.get(BASE_URL + "forecast", params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error occurred: {req_err}")
    return None