from config import *

# Сам сервер
while True:
    request = input("request>")
    print("—" * 48)
    if request == "":
        request = DEFAULT_DOCUMENT

    try:
        with open(DOCUMENT_ROOT + request, encoding=ENCODING, errors="replace") as f:

            doc = f.read()
            # Если это динамическая страница...
            if request.endswith(".py"):
                exec(doc) # Выполняем код в интерпретаторе
            else: # В противном случае, статическая
                # Получаем длину
                doc_size = len(doc.encode(ENCODING))
                # Выводим заголовки
                print("Toy_Server/1.0 200 OK")
                print("Content-type: text/html; charset={}".format(ENCODING))
                print("Content-length: {}".format(doc_size))
                print()
                # Выводим страницу
                print(doc)
    # Обработка разных ошибок
    except FileNotFoundError:
        print("Toy_Server/1.0 404 File Not Found")
    except PermissionError:
        print("Toy_Server/1.0 403 Forbidden")
    except:
        print("Toy_Server/1.0 500 Server Error")
    print("———(response end)———————————————————————————————")
    print()
