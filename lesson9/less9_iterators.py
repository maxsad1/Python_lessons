# итераторы

r = range(0, 5000000)
i = iter(r)
print(next(i))
print(next(i))

data1 = [0,2,3,4,6,8,10]
data2 = [1,3,5,7,9,11,13]
i1 = iter(data1)
i2 = iter(data2)
v1 = next(i1)
v2 = next(i2)

try:
    while True:
        if v1 < v2:
            print(v1)
            v1 = next(i1)
        else:
            print(v2)
            v2 = next(i2)
except StopIteration:
    pass
