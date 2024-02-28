import requests
from dotenv import load_dotenv
import os

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
def welcome_to(name):
    print(f"welcome mr(s) {name}")
    print("to the python weather app wich generate real time weather info about a city")




main()
