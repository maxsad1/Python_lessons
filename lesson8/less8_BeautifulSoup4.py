import requests
from bs4 import BeautifulSoup as BS
from time import sleep
from random import random
from datetime import datetime

print(datetime.now())
sleep(0.5 + 0.5*random())
print(datetime.now())
resp = requests.get('https://anhel.in/python/posts')

if resp.status_code != 200:
    print('error', resp.status_code)
##    exit()

doc = BS(resp.text, 'html.parser')

articles = doc.find_all('article', class_='post')

for art in articles[:5]:
    link = art.h1.a
    link_url = link['href']
    link_text = link.string
    print('{:40}{}'.format(link_text[:40], link_url))
