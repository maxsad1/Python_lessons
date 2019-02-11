def f(a, b, c):
    print(a, b, c)

# распаковка списка (кортежа)
d = [1, 2, 3]
f(d[0], d[1], d[2])
f(*d)

# распаковка словаря
args = {'encoding': 'utf-8', 'mode': 'r'}
f = open('less10_1.py', **args)
f.close()
