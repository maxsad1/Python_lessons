# 
title = 'Hello'
print('*' * 60)
print('*' + title.center(60-2) + '*')
print('*' * 60)

title = 'Привет'
print('*' * 60)
print('*' + title.center(60-2) + '*')
print('*' * 60)

# 
TITLE_WIDTH = 40
TITLE_FRAME_CHAR = '*'

import shutil
def title_print(text, width=None, char='*'):
    """Печать заголовка.
        
        Принимает агрументы:
        Текст заголовка.
        Ширина.
        Символ рамки.
    """
    if width is None:
        ts = shutil.get_terminal_size((80,24))
        width = ts.columns - 1
    print(char * width)
    print(char + text.center(width - 2) + char)
    print(char * width)

title_print('Hello', TITLE_WIDTH, TITLE_FRAME_CHAR)
title_print('Привет', 60, '+')
title_print('Bonjour', 40, '-')
title_print('Hello', char='@', width=20) # Keyword arguments, kw-args
title_print('Ha')

def square(x):
    res = x ** 2
    return res

k = square(89) - square(36)
print(k)

def are_square(side):
    power = 2
    def square(x):
        nonlocal power
        res = x ** power
        return res
    return square(side)

aos = are_square

print(aos(12))

functions = [title_print, are_square, print]

functions[1](23)

f = functions[2]

f('Hello')

def create_multiplier(b=2):
    x = b
    def multiplier(a):
        nonlocal x
        return a * x
    return multiplier

m2 = create_multiplier(3)

print(m2(3))

func = getattr(shutil, 'copyfile')

# func('list.txt', 'list.lst')
people = [
    ('Сидр', 'Андреев'),
    ('Юрий', 'Антонов'),
    ('Петр', 'Петров'),
    ('Иван', 'Иванов'),
    ]

print(sorted(people))

def get_last_name(e):
    return e[1]

print(sorted(people, key=get_last_name))

print(sorted(people, key=lambda e: e[1]))

# lambda x: zzzz -> def _unnamed(): return zzzz

