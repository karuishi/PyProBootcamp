import requests
from bs4 import BeautifulSoup

header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"}
URL = "https://www.billboard.com/charts/hot-100/"
# input("which year do you want to travel to? type the date in this format YYYY-MM-DD: ")
response = requests.get(URL, headers=header)
billboard = response.text
soup = BeautifulSoup(billboard, "html.parser")

hot_100 = soup.find(name="h3", id="title-of-a-story")
print(hot_100.getText())