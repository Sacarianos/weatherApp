import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv('API_KEY')

def get_weather(zip_code, units='metric'):
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={zip_code}&appid={api_key}"
    
    print(url)
    
    response = requests.get(url)

    
    if response.status_code == 200:
        return response.json()  # Returns the weather data as a Python dictionary
    else:
        print(f"Error: {response.status_code}")
        return None