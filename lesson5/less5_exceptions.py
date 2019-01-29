class MyException(Exception):
    pass

def world():
    print('world')
    raise MyException('World exception')
    return 10

def hello():
    print('hello')
    world()
    print('!')


f1 = open('iris.csv', 'r')
try:
    f2 = open('iris.out', 'r')
    hello()
except MyException as e:
    print(f'Ooops! {e}')
except FileNotFoundError as e:
    print(f'File not found: {e}')
    
else:
    print("Ни одного исключения")
finally:
    f1.close


ok = False
while not ok:
    try:
        man_s = int(input("Ваш ход: "))
        ok = True
    except ValueError:
        print("Это не число!")
