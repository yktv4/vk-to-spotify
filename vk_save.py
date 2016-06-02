import vk_api
import json

VK_EMAIL = ''
VK_ID = ''
VK_PASS = ''


def get_sms_code():
    code = raw_input('input code from sms\n')
    print('code received: {}'.format(code))
    return code


def main():
    vk_session = vk_api.VkApi(VK_EMAIL, VK_PASS, auth_handler=get_sms_code)

    try:
        vk_session.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    songs = vk.audio.get(owner_id=VK_ID)['items']

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


if __name__ == '__main__':
    main()
