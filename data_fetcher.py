# data_fetcher.py
import os

import requests
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Fetch the API Key from the environment
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary.
    """
    headers = {"X-Api-Key": API_KEY}

    response = requests.get(f"{BASE_URL}?name={animal_name}", headers=headers)

    if response.status_code == 200:
        return response.json()  # Return the data as a list of dictionaries
    else:
        return []  # Return an empty list if there was an error
