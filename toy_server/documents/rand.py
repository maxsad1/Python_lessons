from random import randint

# Скрипть обязан вывести заголовки
print("Toy_Server/1.0 200 OK")
print("Content-Type: text/html;charset=utf-8")
print() # Пустая строка после заголовка

print("----------------------------")
print("     Случайное число!")
print("----------------------------")
print()
print("В этот раз случайное число:")

n = randint(1, 6)
print(str(n).center(28))

print()
