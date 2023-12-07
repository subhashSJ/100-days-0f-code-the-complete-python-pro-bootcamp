import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

MY_LAT = 48.6901541
MY_LONG = 10.9208893
COUNT = 4

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": os.getenv('API_KEY'),
    'cnt': COUNT,
}

try:
    response = requests.get(
        url=f"https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    weather_data = response.json()
except Exception as e:
    weather_data = []
    print(e)

if len(weather_data) > 0:
    for item in weather_data['list']:
        if item["weather"][0]["id"] < 700:
            print("Bring an umbrell")
            break
