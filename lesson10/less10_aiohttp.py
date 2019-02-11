import asyncio
import aiohttp
import json
import requests
from time import monotonic as mt

URL = 'http://jsonplaceholder.typicode.com/albums/{}'

async def fetch_album(idx, session):
    global URL
    url = URL.format(idx)
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            # response.text() - текст
            # response.content() - файлы - картинки например
            return data
        print(f'Error fetching index {idx}')
        return None

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_album(i, session))
                 for i in range(1, 101)]
        data = await asyncio.gather(*tasks)
        # for d in data:
        #     if d:
        #         print(d['title'])

print('Asynchronous requests')
t = mt()
asyncio.run(main())
print('Finishing in {} sec.'.format(mt()-t))
