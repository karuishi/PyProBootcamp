import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials

try:
    # This automatically looks for the environment variables we just exported
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    print("Succesfully connected to Spotify!\n")
    
    artist_name = "Radiohead"
    print(f"Searching for: {artist_name}...")
    
    results = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
    items = results['artists']['items']
    
    if items:
        artist = items[0]
        print(f"Found Artist: {artist['name']}")
        print(f"Followers:    {artist['followers']['total']:,}")
        print(f"Genres:       {', '.join(artist['genres'])}")
        print(f"Spotify URI:  {artist['uri']}")
    else:
        print("No artist found.")

except Exception as e:
    print(f"An error occurred: {e}")