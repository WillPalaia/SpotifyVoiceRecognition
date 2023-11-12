import spotipy
from spotipy.oauth2 import SpotifyOAuth
from main import *

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

    def addtoqueue_spotify(self, title, artist):
        devices = self.spotify.devices()
        song = self.search_song(title, artist)
        for device in devices['devices']:
            self.spotify.add_to_queue(song, device['id'])
    
    def rewind_spotify(self):
        devices = self.spotify.devices()
        for device in devices:
            if device['is_active']:
                self.spotify.previous_track(device['id'])

    def replay_song(self):
        self.rewind_spotify()
        self.skip_spotify()

    def search_song(self, title, artist):
        song = self.spotify.search(title + ' ' + artist, limit=1, offset=0, type='track', market=None)
        return song['tracks']['items'][0]['uri'][14::]
    
    def search_album(self, title, artist):
        album = self.spotify.search(title + ' ' + artist, limit=1, offset=0, type='album', market=None)
        return album['albums']['items'][0]['uri'][14::]
    
    def search_artist(self, artist):
        self.artist = self.spotify.search(artist, limit=1, offset=0, type='artist', market=None)
        return self.artist['artists']['items'][0]['name']#[14::]
        
    def play(self, uri, play_type):
        
        if play_type == 'song':
            uris = [f'spotify:track:{uri}']
            devices = self.spotify.devices()
            for device in devices['devices']:
                if device['is_active']:
                    self.spotify.start_playback(device_id = device['id'], uris = uris)
        if play_type == 'album':
            c_uri = f'spotify:album:{uri}'
            devices = self.spotify.devices()
            for device in devices['devices']:
                if device['is_active']:
                    self.spotify.start_playback(device_id = device['id'], context_uri = c_uri)

test = Functions()
print(test.search_album('Graduation', 'Kanye West'))
print(test.search_song('Money Trees', 'Kendrick Lamar'))
print(test.search_artist('Taylor Swift'))
