import json
import requests
from time import monotonic as mt

URL = 'http://jsonplaceholder.typicode.com/albums/{}'

def fetch_album(idx, session):
    global URL
    url = URL.format(idx)
    resp = session.get(url)
    if resp.status_code == 200:
        data = json.loads(resp.text)
        return data
    print(f'Error fetching index {idx}')
    return None

def main():
    session = requests.Session()
    data = [fetch_album(i, session)
            for i in range(1, 101)]

print('Synchronous requests')
t = mt()
main()
print('Finishing in {} sec.'.format(mt()-t))
