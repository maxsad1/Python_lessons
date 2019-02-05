import json
import requests

URL = 'http://jsonplaceholder.typicode.com/posts/'

def get_post(post_id):
    print('Получаю данные с адреса', URL + str(post_id))
    resp = requests.get(URL + str(post_id))
    data = json.loads(resp.text)
    return data

for post_id in range(1, 51):
    post = get_post(post_id)
    print(post['title'])
