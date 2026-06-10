import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self._users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.users_data = {}

    def get_destination_data(self):
        response = requests.get(url=self._prices_endpoint, auth=self._authorization)
        data = response.json()
    
        if "prices" not in data:
            print("Error fetching data:", data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self._prices_endpoint}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)

    def get_customer_email(self):
        response = requests.get(url=self._users_endpoint, auth=self._authorization)
        data = response.json()
        self.users_data = data["users"]
        return self.users_data
        