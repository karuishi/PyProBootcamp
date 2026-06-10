import requests
import spotipy 
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"}
url = "https://www.billboard.com/charts/hot-100/"
spotify_client_id = "89c7144119a644abb71d3555c9d21f83"
spotify_client_secret = "5d1ecbcb6539473db9a4adbe0b6408ae"
spotify_cliente_uri = "https://example.com"

# date = input("which year do you want to travel to? type the date in this format YYYY-MM-DD: ")

# Billboard Scrapping
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
#print(song_names)
  
# Spotify Authentication
scope = "playlist-modify-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        redirect_uri=spotify_cliente_uri,
        cache_path="token.txt"))

user_id = sp.current_user()["id"]
# print(user_id)

song_uris = []
print("Searching Spotify for song URIs...")

for song in song_names:
    result = sp.search(q=f"track: {song}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"'{song}' does not exist in Spotify. Skipped.")

print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name="Billboard Hot 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)