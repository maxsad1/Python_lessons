import requests
from bs4 import BeautifulSoup
from time import sleep
from random import random

# 1. Получаем HTML-текст страницы
resp = requests.get("https://anhel.in/python/posts/")
# 2. Проверяем, что всё в порядке
if resp.status_code != 200:
    print("Сервер ответил", resp.status_code)
    exit()
# 3. Разбираем полученный HTML
doc = BeautifulSoup(resp.text, "html.parser")
# 4. Ищем информацию
# Получаем список тегов <article>
articles = doc.find_all("article", class_="post")
# Перебираем их (первые пять штук)
for art in articles[:5]:
    link = art.h1.a # Извлекаем тег <a> в теге <h1>
    link_url = link["href"] # Получаем значение атрибута href= у этого тега <a>
    link_text = link.string # Получаем текст, который внутри тега <a>
    print("{:40} | {}".format(link_text[:40], link_url))
