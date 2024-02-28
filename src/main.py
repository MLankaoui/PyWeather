import requests
from dotenv import load_dotenv
import os
from coordinates import display_city_cooredinates
from weather_infos import display_weather_infos

load_dotenv()  # take environment variables from .env.
api_key = os.getenv('API_KEY')

city = ""

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},uk&appid={api_key}")

weather = response.json()

def main():
    print("hello welcome welcome to the python weather app !")

    user_name = input("please enter a user_name : ")

    while user_name == "":
        user_name = input("please enter a user_name : ")

    else:
        welcome_to(user_name)

    option_message()

    while(True):
        input_field = input("> ").lower()

        if input_field == "options":
            print("1) to see the coordinates of your chosen city")
            print("2) to see weather informations")
            print("3) to see the base")
            print("4) to see main informations")
            print("5) to see visibility")
            print("6) to see the city overall informations")
            print('and please enter quit if you want to exit the program')

        elif input_field == 'quit':
            print('exiting...')
            exit(1)
        elif input_field == '1':
            city = input("enter the city name : ")
            display_city_cooredinates(city)
            option_message()

        elif input_field == '2':
            city = input("enter the city name : ")
            display_weather_infosM(city)
            option_message()

def welcome_to(name):
    print(f"welcome mr(s) {name}")
    print("to the python weather app which generates real-time weather info about a city")

def option_message():
    print("options to see the available options")

main()
