import requests
from twilio.rest import Client

api_key = "f7965c8788ff011135f9b7024f19011b"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "ACa946676f464329e90f3cf56cc0d32630"
auth_token = "1be6f4ee2143e1f00b5d09a62682965e"

params = {
    "lat": -12.977749,
    "lon": -38.501629,
    "appid": api_key,
    "cnt": 4, # next 12-hour window
}

response = requests.get(OWM_endpoint, params)
print(f"Status code: {response.status_code}")
response.raise_for_status()
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="It's going to rain today. Remember to bring an umbrella",
    from_="+16206757407",
    to="+5571988360935",
    )
    print(message.status)