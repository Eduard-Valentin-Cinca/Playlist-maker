import spotipy
from spotipy.oauth2 import SpotifyOAuth
from web_scrapping import track_names
import json

scope = 'playlist-modify-public'
username = 'yedwtzzu'

token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

playlist_name = 'beatport-top-100'
playlist_description = 'Top 100 tracks from beatport.com'

spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

list_of_songs = []

for song in track_names:
    result = spotifyObject.search(q=song)
    list_of_songs.append(result['tracks']['items'][0]['uri'])

prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=list_of_songs)
