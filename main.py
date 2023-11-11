from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
from spotipy import Spotify

"""
CLIENT_ID = "5d3a61ce96b245adaf521468e1b8ed55"
CLIENT_SECRET = "af2ea7921189463abfe526725b9ea465"
"""

def get_album_uri(spotify: Spotify, name: str) -> str:
    """
    :param spotify: Spotify object to make the search from
    :param name: album name
    :return: Spotify uri of the desired album
    """

    # Replace all spaces in name with '+'
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='album')
    if not results['albums']['items']:
        raise NameError(f'No album named "{original}"')
    album_uri = results['albums']['items'][0]['uri']
    return album_uri

def get_artist_uri(spotify: Spotify, name: str) -> str:
    """
    :param spotify: Spotify object to make the search from
    :param name: album name
    :return: Spotify uri of the desired artist
    """

    # Replace all spaces in name with '+'
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='artist')
    if not results['artists']['items']:
        raise NameError(f'No artist named "{original}"')
    artist_uri = results['artists']['items'][0]['uri']
    print(results['artists']['items'][0]['name'])
    return artist_uri

def get_track_uri(spotify: Spotify, name: str) -> str:
    """
    :param spotify: Spotify object to make the search from
    :param name: track name
    :return: Spotify uri of the desired track
    """

    # Replace all spaces in name with '+'
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='track')
    if not results['tracks']['items']:
        raise NameError(f'No track named "{original}"')
    track_uri = results['tracks']['items'][0]['uri']
    return track_uri

def play_album(spotify=None, device_id=None, uri=None):
    spotify.start_playback(device_id=device_id, context_uri=uri)


def play_artist(spotify=None, device_id=None, uri=None):
    spotify.start_playback(device_id=device_id, context_uri=uri)


def play_track(spotify=None, device_id=None, uri=None):
    spotify.start_playback(device_id=device_id, uris=[uri])
    

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def currently_playing(token):
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    print(result)
    

token = get_token()
currently_playing(token)