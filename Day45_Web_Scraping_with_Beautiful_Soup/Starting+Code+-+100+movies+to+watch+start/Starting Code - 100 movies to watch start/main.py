import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movie_webpage = response.text
soup = BeautifulSoup(movie_webpage, "html.parser")

all_h3_tags = soup.find_all("h3", "title")

movie_list = [tag.getText() for tag in all_h3_tags]
top_100_movies = movie_list[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in top_100_movies:
        file.write(f"{movie}\n")
