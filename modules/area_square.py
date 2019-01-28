def area_square(side):
    power = 2
    def square(x):
        nonlocal power
        res = x ** power
        return res
    return square(side)
