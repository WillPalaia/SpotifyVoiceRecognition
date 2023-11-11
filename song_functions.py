import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Functions:
    def __init__(self) -> None:
        self.client_id = '5d3a61ce96b245adaf521468e1b8ed55'
        self.client_secret = 'af2ea7921189463abfe526725b9ea465'
        self.redirect_uri = 'http://localhost:3000'
        self.SCOPEs = ['app-remote-control', 'user-read-playback-state', 'user-modify-playback-state']
        self.auth_manager = SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope=self.SCOPEs,
            username='tocarmeli'
        )

        self.spotify = spotipy.Spotify(auth_manager=self.auth_manager)
    
    def pause_spotify(self):
        devices = self.spotify.devices()
        for device in devices['devices']:
            self.spotify.pause_playback(device['id'])

    def resume_spotify(self):
        devices = self.spotify.devices()
        print(devices)
        for device in devices['devices']:
            self.spotify.start_playback(device['id'])


    def skip_spotify(self):
        devices = self.spotify.devices()
        for device in devices['devices']:
            self.spotify.next_track(device['id'])



test = Functions()
test.pause_spotify()