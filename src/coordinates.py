import requests
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
api_key = os.getenv('API_KEY')


def display_city_cooredinates(city_name):
    print('So you chose to display the coordinates of your chosen city.')

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name},uk&appid={api_key}")

    if response.status_code == 404:
        print(f"The city '{city_name}' was not found in the API.")
        return

    weather = response.json()

    print(f"Longitude: {weather['coord']['lon']}")
    print(f"Latitude: {weather['coord']['lat']}")