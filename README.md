# SpotifyVoiceRecognition
Asks user to say a function done within Spotify (e.g., skip, rewind, pause, etc.) and will recognize what has been said and perform the function using Spotify's API

Uses OAUTH 2.0 along with Spotipy and Voice Recognition Python libraries.

## Usage
### Command Line Interface:
When running `main_code_run.py`, speak into microphone one of the following commands from [Available Functions](https://github.com/tocarmeli/SpotifyVoiceRecognition/edit/main/README.md#available-functions). The command inputted will then be outputted via terminal to confirm what has been said. 
### Available Functions:
- Resume
- - Resumes song that is currently paused
- Pause
- - Pauses current song
- Skip
- - Skips current song
- Add to queue
- - Adds specific song to queue
  - Function called as `Add *song name* by *song artist*`
- Rewind
- - Goes back and plays song that was played immediately before current song
- Replay
- - Replays current song
- Play
- - Plays specific song given either song title, artist, or album
  - Function called as either:
  - - `Play *song name* by *song artist*`
    - `Play *album name* by *song artist*`
