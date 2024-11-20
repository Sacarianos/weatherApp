import requests
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv('API_KEY')

def get_weather(zip_code, units='metric'):

    
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




def display_forecast(forecast_data):
    if forecast_data:
        day = ""
        for forecast in forecast_data.get('list', []):
            dt_txt = forecast.get('dt_txt')
            # Parse the input string into a datetime object
            date_object = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")
            if day != date_object.strftime("%d"):
                print(f"\nDate: {date_object.strftime("%Y-%m-%d")}")
                day = date_object.strftime("%d")
        
            hour = date_object.strftime("%H")

            temp = forecast.get('main', {}).get('temp')
            description = forecast.get('weather', [{}])[0].get('description')
            print(f"{hour}H - {temp}° - {description.capitalize()}")
                                          


def get_forecast(zip_code, units='metric'):
    base_url = 'http://api.openweathermap.org/data/2.5/forecast'
    
    params = {
        'zip': zip_code,
        'appid': api_key,
        'units': units  # 'metric' for Celsius, 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()  # Returns the forecast data as a Python dictionary
    else:
        print(f"Error: {response.status_code}")
        return None