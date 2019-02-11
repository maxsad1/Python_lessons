import asyncio
from random import uniform, choice
from time import monotonic, sleep


MENU = ['Борщ', 'Котлеты', 'Плов', 'Манты']

async def cook_order(order, num):
    print(f'Кухня готовит "{order}" для столика {num}')
    await asyncio.sleep(uniform(5, 15))
    result = '"{}" готов'.format(order)
    print(f'Кухня: {result} для столика {num} можно забирать!')
    return result

async def bring_menu():
    await asyncio.sleep(uniform(1, 3))
    return MENU

async def make_order(menu, num):
    print(f'Столик {num} думает...')
    await asyncio.sleep(uniform(2, 5))
    # Что будет, если обратиться к синхронным методам
    # sleep(5)
    # Программа будет затуплять
    # Если заэвейтить не эвейт объект будет ошибка
    # TypeError: object NoneType can't be used in 'await' expression
    # await sleep(5)
    return choice(menu)

async def serve_table(num):
    print(f'Добро пожаловать, столик {num}. Сейчас принесу меню.')
    menu = await bring_menu()
    # а так не надо
    # sleep_coro = asyncio.sleep(uniform(1, 3))
    # res = await sleep_coro
    print(f'Вот ваше меню, столик {num}. Сообщите когда будете готовы заказать.')
    # order = await make_order(menu, num)
    # с ограничением времени
    try:
        order = await asyncio.wait_for(make_order(menu, num), 3)
    except asyncio.TimeoutError:
        print(f'Столик {num} не успел')
        order = 'Ничего'
    print(f'Столик {num} выбрал "{order}". Сообщу на кухню. Пусть готовят.')
    food = await cook_order(order, num)
    print(f'Столик {num}, ваш заказ: {food}, приятного аппетита!')
    await asyncio.sleep(uniform(2, 5))
    print(f'Столик {num}, вот ваш счет, приходите еще!')
    print(f'Столик {num} обслужен.')

async def supervisor(tasks):
    while True:
        await asyncio.sleep(2)
        done_tasks = [t for t in tasks if t.done()]
        print('....Выполнено задач {} из {}'.format(len(done_tasks), len(tasks)))
        if len(done_tasks) + 1 == len(tasks):
            return

async def async_main():
    """ Заметки
    # Подключение к текущей задаче
    t = asyncio.current_task()
    # Отмена задачи
    t.cancel
    # 
    if t.done():
        res = t.result() # if task success done
    else:
        res = t.exception() # if task failed
    # 
    if t.cancelled():
        ...
    # Таймаут на выполнение задачи
    # после await можно использовать
    try:
        await asyncio.wait_for(task, 5)
    except asyncio.TimeoutError:
        print('Не успел')
    """
    # Можно так
    # for num in range(1, 4):
    #     task = asyncio.create_task(serve_table(num))
    #     tasks.append(task)

    # Лучше использовать генератор списков
    tasks = [asyncio.create_task(serve_table(num)) for num in range(1, 4)]

    # Можно так
    # await asyncio.gather(serve_table(1), serve_table(2), serve_table(3))
    # Лучше использовать распаковку списков, кортежей
    await asyncio.gather(*tasks, supervisor(tasks))


# Асинхронное выполнение
t = monotonic()
asyncio.run(async_main())
print('Async: {} sec.'.format(monotonic()-t))



# Синхронное выполнение

# async def sync_main():
#     for i in range(1, 4):
#         await serve_table(i)

# t = monotonic()
# asyncio.run(sync_main())
# print('Async: {} sec.'.format(monotonic()-t))
