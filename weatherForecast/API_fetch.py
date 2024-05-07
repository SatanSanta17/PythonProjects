import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY2")

def get_current_weather(city):
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={API_KEY}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        print("Error fetching current weather data.")
        return None

def get_weather_forecast(city):
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={city}&apikey={API_KEY}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    data = response.json()

    if response.status_code == 200:
        return data
    else:
        print("Error fetching weather forecast data.")
        return None

def get_hourly_weather(city):
    url = f"https://api.tomorrow.io/v4/weather/history/recent?location={city}&apikey={API_KEY}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        print("Error fetching weather forecast data.")
        return None