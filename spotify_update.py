import time
import json
import spotify

# NOTE: you should have your binary libspotify key in this folder
# and libspotify installed
SPOTIFY_LOGIN = ''
SPOTIFY_PASS = ''
PLAYLIST_URI = ''

session = spotify.Session()
session.login(SPOTIFY_LOGIN, SPOTIFY_PASS)

while session.connection.state != 1:
    print('Logging in...')
    session.process_events()
    time.sleep(1)

print('Logged in as {}'.format(session.user))

playlist = session.get_playlist(PLAYLIST_URI)
playlist.load()
print('Working with {} playlist'.format(playlist.name))

songs = []
with open('songs.json', 'r') as f:
    songs = json.load(f)

spotify_tracks = []
for i, song in enumerate(songs):
    print('Searching {}/{} - {} {}'.format(
        i, len(songs),
        song['artist'], song['title']
    ))
    search = session.search('{} {}'.format(song['artist'], song['title']))
    search.load()
    if len(search.tracks):
        track = search.tracks[0].load()
        spotify_tracks.append(track)
        print('Found')
    else:
        print('Not found')

print('Adding tracks...')
playlist.add_tracks(spotify_tracks)
retries = 10
while retries:
    session.process_events()
    time.sleep(2)
    retries -= 1
print('Completed, added {}, missed {}'.format(
    len(spotify_tracks),
    len(songs) - len(spotify_tracks)
))
