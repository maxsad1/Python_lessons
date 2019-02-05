# def make_evens_gen(n):
#     print('Создан генератор на {} чисел'.format(n))
#     for i in range(n):
#         print('Генератор выдал число', i)
#         yield i * 2

# r = make_evens_gen(10)

# for k in r:
#     print('********', k)

import timeit

# Список
# Так не годится. Много лишних объектов.
def make_evens(n):
    res = []
    for i in range(n):
        res.append(i*2)
    return res

# # Выполняется быстро
print(timeit.timeit('sum(make_evens(50))', 
    setup="from __main__ import make_evens", number=10))

# # Уже медленно
print(timeit.timeit('sum(make_evens(5000000))', 
    setup="from __main__ import make_evens", number=10))

# Следует использовать генераторы
# Генератор
def make_evens_gen(n):
    for i in range(n):
        yield i * 2 # yield делает из функции генератор

# Списком Медленно
print(timeit.timeit('sum(make_evens(5000000))', 
    setup="from __main__ import make_evens", number=10))

# Генератор работает Быстрее в 1.5 раза
print(timeit.timeit('sum(make_evens_gen(5000000))', 
    setup="from __main__ import make_evens_gen", number=10))
