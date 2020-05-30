import csv
import requests


token = 'fd0a0c21fd0a0c21fd0a0c21c4fd7841cdffd0afd0a0c21a3d87c7425055109b33d4954'
version = 5.107
owner_id = int(input('Введите id, чьи альбомы вы хотите просмотреть: '))


def get_all_albums(o_id):
    response = requests.get('https://api.vk.com/method/photos.getAlbums',
                            params={'access_token': token,
                                    'v': version,
                                    'owner_id': o_id,
                                    'fields': 'domain'})
    data = response.json()
    return data


def albums2list(data):
    albums_list = [f"{album['title']}" for album in data['response']['items']]
    with open(f'albums_of_{owner_id}.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(f'Альбомы id {owner_id}')
        for i in albums_list:
            a_pen.writerow(i)
    print('Файл с альбомами записан!')


data = get_all_albums(owner_id)
albums2list(data)
