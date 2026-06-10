import requests
from datetime import datetime

TOKEN = "farcry34"
USERNAME = "karuishi"
GRAPH_ID = "graph1"

pixela_endpoint = " https://pixe.la/v1/users"
user_params = {
    "token": "farcry34",
    "username": "karuishi",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Studying Hours Graph",
    "unit": "hours",
    "type": "int",
    "color": "ajisai",
}
# Advanced authentication using an HTTP header
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today? "),
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "6" 
}
# response = requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

yesterday = datetime(2026, 2, 19)
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)