import random


def turn(sticks):
    """Number of sticks which computer takes
    """
    if sticks < 1:
        raise ValueError("Invalid number of sticks")
    if sticks == 1:
        return 1
    if sticks < 4:
        return sticks - 1
    takes = (sticks - 1) % 4
    if takes == 0:
        return random.randint(1, 3)
    return takes


def user_input(sticks, inp_func=input):
    """Return user turn
    """
    print("Осталось: ", sticks)
    while True:
        try:
            val = int(inp_func("Сколько берете?"))
        except ValueError:
            print("Введите число")
            continue
        if val < 1 or val > 3:
            print("Можно брать только от 1 до 3")
            continue
        if val > sticks:
            print("Нельзя взять больше, чем есть")
            continue
        return val
