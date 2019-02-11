import aiofiles
import asyncio
import os

DIR = r'D:\MyDocs\python\homework\library_dir\library'

async def process_file(name):
    chars = {}
    args = {'mode': 'r', 'encoding': 'utf-8'}
    async with aiofiles.open(name, **args) as f:
        async for line in f:
            for char in list(line.strip()):
                char = char.lower()
                chars[char] = chars.setdefault(char, 0) + 1
    return chars

async def main():
    global DIR
    files = [elem.path for elem in os.scandir(DIR) 
                            if elem.is_file()
                            if elem.name.endswith('.txt')
                            if elem.name != 'description.txt']
    tasks = []
    for name in files:
            tasks.append(process_file(name))
    res = await asyncio.gather(*tasks)
    hist = {}
    for elem in res:
        for char, cnt in elem.items():
            hist[char] = hist.setdefault(char, 0) + cnt
    sort_key = lambda k: k[1]
    hist_list = (elem for elem in sorted(list(hist.items()), key=sort_key, reverse=True)) 
    for char, cnt in hist_list:
        print(f'Символ "{char}" встречается {cnt} раз.')

asyncio.run(main())
