import requests
import csv


token = 'fd0a0c21fd0a0c21fd0a0c21c4fd7841cdffd0afd0a0c21a3d87c7425055109b33d4954'
version = 5.107
user_id = int(input('Введите id пользователя (число): '))


def get_all_friends(u_id):
    response = requests.get('https://api.vk.com/method/friends.get',
                            params={'access_token': token,
                                    'v': version,
                                    'user_id': u_id,
                                    'fields': 'domain'})
    data = response.json()
    return data


def friends2list(data):
    friend_list = [f"{friend['first_name']} {friend['last_name']}" for friend in data['response']['items']]
    with open(f'friends_of_{user_id}.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('First name', 'Last name'))
        count_of_deleted = 0
        for friend in friend_list:
            fr = friend.split()
            if fr[0] != 'DELETED':
                a_pen.writerow((fr[0], fr[1]))
            else:
                count_of_deleted += 1
        a_pen.writerow((f'Всего друзей: {len(friend_list)}', f'Друзей, удаливших страницу: {count_of_deleted}'))
    print(f'Записан файл с друзьями friends_of_{user_id}.csv!')


data = get_all_friends(user_id)
friends2list(data)
