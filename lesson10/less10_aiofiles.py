import aiofiles
import asyncio
import os

DIR = r'D:\MyDocs\python\homework\library_dir\library'

async def process_file(name, char):
    commas = 0
    args = {'mode': 'r', 'encoding': 'utf-8'}
    async with aiofiles.open(name, **args) as f:
        async for line in f:
            commas += line.count(char)
        # Чтение файла целиком
        # text = await f.read()
    return char, commas

async def main():
    global DIR
    chars = ['а', 'б', ',', '.']
    files = [elem.path for elem in os.scandir(DIR) 
                            if elem.is_file()
                            if elem.name.endswith('.txt')
                            if elem.name != 'description.txt']
    tasks = []
    for name in files:
        for char in chars:
            tasks.append(process_file(name, char))
    res = await asyncio.gather(*tasks)
    hist = {}
    for char, cnt in res:
        hist[char] = hist.get(char, 0) + cnt
    sort_key = lambda k: k[1]
    hist_list = list(hist.items())
    print(sorted(hist_list, key=sort_key))
    
    # async with aiofiles.open('out.txt', 'w', encoding='utf-8') as out:
        # await out.write('{} в библиотеке: {}'.format(charsum(res)))

asyncio.run(main())
