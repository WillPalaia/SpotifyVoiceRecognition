import requests
import datetime
import time
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your Spotify app credentials (client ID and client secret)
client_id = '5d3a61ce96b245adaf521468e1b8ed55'
client_secret = 'af2ea7921189463abfe526725b9ea465'
redirect_uri = 'http://localhost:3000' # my demo use http://localhost:3000/callback

# scopes for Remote control playback, Get Available Devices, Pause playback
SCOPEs = ['app-remote-control', 'user-read-playback-state', 'user-modify-playback-state']
auth_manager = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=SCOPEs,
    username='tocarmeli'
)
spotify = spotipy.Spotify(auth_manager=auth_manager)

def pause_spotify():
    devices = spotify.devices()
    for device in devices['devices']:
        if device['is_active']:
            spotify.pause_playback(device['id'])

def resume_spotify():
    devices = spotify.devices()
    print(devices)
    for device in devices['devices']:
        if device['is_active']:
            spotify.start_playback(device['id'])



resume_spotify()