import requests as reqs
import re
from bs4 import BeautifulSoup

resp = reqs.get('http://bash.im')
print(resp.status_code)
if resp.status_code != 200:
    print('Ошибка загрузки')

##    resp.encoding
##    resp.url
##    resp.content
##    resp.text

with open('bash.html', 'w', encoding='windows-1251') as f:
    f.write(resp.text)

## Найти количество утвержденных сегодня цитат

## Вот так делать не надо
t = resp.text
pos = t.find('<div id="stats">')

print(pos)

frag = t[pos:pos+40]
print(frag)

rexp = re.compile(r'\d+')
m = rexp.search(frag)
print(m.group())

## Надо использовать специальные билиотеки для парсинга HTMP
## BeautifulSoup4 например

bs = BeautifulSoup(resp.text, 'html.parser')
print(bs.prettify()[:200])

d = bs.div

div = bs.find(id='stats').b

print(div)


