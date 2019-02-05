# Замер времени
import timeit

def test1():
    res = [[3 for x in range(50)] for x in range(50)]

print(timeit.timeit("test1()", setup="from __main__ import test1", number=1))