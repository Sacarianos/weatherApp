import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv('API_KEY')

def get_weather(zip_code, units='metric'):

    units = "imperial"
    
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={api_key}&units={units}"
    
    response = requests.get(url)

    
    if response.status_code == 200:
        return response.json()  # Returns the weather data as a Python dictionary
    else:
        print(f"Error: {response.status_code}")
        return None

def display_weather(weather_data):
    if weather_data:
        main = weather_data.get('main', {})
        weather = weather_data.get('weather', [{}])[0]
        sys = weather_data.get('sys', {})
        temp = main.get('temp')
        description = weather.get('description')
        city = weather_data.get('name')
       
        print(f"This is the weather forecast for {city}")
        print(f"Temperature: {temp}°")
        print(f"Description: {description.capitalize()}")