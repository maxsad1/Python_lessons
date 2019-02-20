import asyncio
import aiohttp
from bs4 import BeautifulSoup as BS
from time import monotonic as mt

URL = 'https://bash.im/'


async def fetch_html(session):
    global URL
    async with session.get(URL) as response:
        if response.status == 200:
            data = await response.text()
            # response.json()
            # response.text() - текст
            # response.content() - файлы - картинки например
            return data
        print(f'Error fetching {response.status}')
        return None


async def cities_count(session):
    html = await fetch_html(session)
    soup = BS(html, "html.parser")
    div = soup.find(id="stats")
    if div:
        count_s = div.b.string
        try:
            count = int(count_s)
        except ValueError:
            count = -1
        return count
    return -1


async def main():
    async with aiohttp.ClientSession(trust_env=True) as session:
        # Если сертификат сервера не нравится aiohttp, то можно отключить ssl
        # conn = aiohttp.TCPConnector(ssl=False)
        # async with aiohttp.ClientSession(connector=conn) as session:
        count = await cities_count(session)
        print('Count:', count)


print('Asynchronous requests')
t = mt()
asyncio.run(main())
print('Finishing in {} sec.'.format(mt() - t))
