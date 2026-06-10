import requests, pprint, os
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/62d399f69508f59627b49c3579d848b7/flightDeals2026/prices"

class DataManager():
    def __init__(self):
        self._token = os.environ["SHEETY_TOKEN"]
        self._authorization = {"Authorization": f"Bearer {self._token}"}
        self.destination_data = {}
        
    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=self._authorization)
        data = response.json()
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
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self._authorization
            )
            pprint.pp(response.text)
    
    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{row_id}", json=new_data, headers=self._authorization)
        print(f"Updated row {row_id} with new lowest price: {new_price}")
        pprint.pp(response.text)