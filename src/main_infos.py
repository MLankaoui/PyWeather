import requests
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
api_key = os.getenv('API_KEY')

def display_main_infos(city_name):
    print('So you chose to display the weather infos of your chosen city.')

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")

    if response.status_code == 404:
        print(f"The city '{city_name}' is not available for the moment!")
        return

    weather = response.json()

    print(f"temp: {weather['main']['temp']} K")
    print(f"feels_like: {weather['main']['feels_like']} K")
    print(f"temp_min: {weather['main']['temp_min']} K")
    print(f"temp_max: {weather['main']['temp_max']} K")
    print(f"pressure: {weather['main']['pressure']} hPa")
    print(f"humidity: {weather['main']['humidity']}%")
