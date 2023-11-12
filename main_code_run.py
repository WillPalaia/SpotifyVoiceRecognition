from spotipy.oauth2 import SpotifyOAuth
import speech_recognition as sr
import spotipy
import song_functions

command = song_functions.Functions()

#Connecting to spotify
auth_manager = SpotifyOAuth(client_id = command.client_id, 
                            client_secret = command.client_secret, 
                            redirect_uri = command.redirect_uri, 
                            scope = command.SCOPEs)
spotify = spotipy.Spotify(auth_manager = auth_manager)

recognizer = sr.Recognizer()

while True:
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source=source)
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except:
        continue

    list_word = text.split(" ")
    list_word[0] = list_word[0].lower()
    if list_word[0] == 'pause':
        command.pause_spotify()
    elif list_word[0] == 'resume':
        command.resume_spotify()
    elif list_word[0] == 'replay':
        command.replay_song()
    elif list_word[0] == 'skip':
        command.skip_spotify()
    elif list_word[0] == 'rewind':
        command.rewind_spotify()
    elif "add to queue" in text:
        author_name = ''
        song_album_name = ''
        for i,word in enumerate(list_word):
            if word == 'by':
                author_name = ' '.join(list_word[i+1:])
                song_name = ' '.join(list_word[3:i+1])
                break
        command.addtoqueue_spotify(title=song_album_name, artist=author_name)
    elif list_word[0] == 'play':
        author_name = ''
        song_album_name = ''
        for i,word in enumerate(list_word):
            if word == 'by':
                author_name = ' '.join(list_word[i+1:])
                song_album_name = ' '.join(list_word[2:i])
                break
        if list_word[1] in ('track', 'song'):
            uri = command.search_song(song_album_name, author_name)
            command.play(uri, 'song')
        elif list_word[1] == "album":
            uri = command.search_album(song_album_name, author_name)
            command.play(uri, 'album')
    else:
        print("Unknown Command")
