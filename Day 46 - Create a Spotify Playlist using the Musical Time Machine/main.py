import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "0d77e41d46c84ca1b884cfa556e9580c"
CLIENT_SECRET = "a723dab13ed948db9db5e060300c286c"

url = "https://www.billboard.com/charts/hot-100"

date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"{url}/{date}")

soup = BeautifulSoup(response.text, 'html.parser')
song_names = [song.get_text().strip() for song in soup.select("li ul li h3")]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Subhash Jadhav"
    )
)

user_id = sp.current_user()["id"]

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
