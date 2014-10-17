import vk
import json

VK_APPID = ''
VK_EMAIL = ''
VK_PASS = ''

vkapi = vk.API(VK_APPID, VK_EMAIL, VK_PASS, scope='audio')

songs = vkapi.audio.get()['items']

print('You have {} songs'.format(len(songs)))

with open('songs.json', 'w') as f:
    to_dump = []
    for song in songs:
        to_dump.append({
            'artist': song['artist'],
            'title': song['title'],
        })

    json.dump(to_dump, f)

print('Saved to songs.json')

