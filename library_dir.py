import os

def read_library_description(library_dir):
    """Поиск и чтение файла description.txt

    Формат функции:
    read_library_description(library_dir)

    Функция находит в папке с библиотекой файл description.txt и возвращает содержание этого файла. Если файла нет или его невозможно прочитать, возвращает пустую строку."""

    desc_file = os.path.join(library_dir, 'description.txt')
    content = ''
    try:
        with open(desc_file, 'r', encoding='utf-8') as f:
            content = [line.replace('\n', '') for line in f]
    except Exception as e:
        pass
    finally:
        return content


def get_book_files(library_dir):
    """Возвращает список имён файлов книг в указанной папке.

    Формат функции:
    get_book_files(library_dir):

    Функция возвращает список имён файлов книг в указанной папке."""
    
    books_list = []
    try:
        for f in os.listdir(library_dir):
            if os.path.isfile(os.path.join(library_dir, f)):
                if f.endswith('.txt') and f != 'description.txt':
                    books_list.append(f)
    except Exception as e:
        # print('Error', e)
        pass
    finally:
        return books_list


def read_book_info(library_dir, book_file):
    """Возвращает кортеж из трёх значений: (автор, название, аннотация)

    Формат функции:
    read_book_info(library_dir, book_file)

    Параметры:
    library_dir – папка библиотеки
    book_file – имя файла с книгой

    Функция возвращает кортеж из трёх значений: (автор, название, аннотация)."""

    author, title, annotation = '', '', ''
    try:
        with open(os.path.join(library_dir, book_file), 'r', encoding='utf-8') as f:
            author = f.readline().replace('\n', '').strip('. ')
            title = f.readline().replace('\n', '').strip(' ')
            annotation = f.readline().replace('\n', '').strip(' ')
    except Exception as e:
        # print('Error is:', e)
        pass
    finally:
        return (author, title, annotation)

def get_authors(library_dir):
    """Возвращает список имён авторов, книги которых есть в библиотеке.

    Формат функции:
    get_authors(library_dir)

    Функция возвращает список имён авторов, книги которых есть в библиотеке. Имена в списке не должны повторяться, конечно. Для этого придётся пройти по списку файлов книг и прочитать имя автора из каждой книги. Например, для имеющегося в наличии примера результат должен быть такой:

    ["Александр Сергеевич Пушкин", "Николай Васильевич Гоголь"]"""

    authors = []
    books_list = get_book_files(library_dir)
    for book in books_list:
        author = read_book_info(library_dir, book)
        authors.append(author[0])
    return (sorted(set(authors)))


def get_all_books_info(library_dir):
    """Возвращает список книг c описанием в данной папке.

    Формат функции:
    get_all_books_info(library_dir)

    Эта функция возвращает список книг в данной папке, причём каждая книга представлена в виде кортежа (автор, название, аннотация, имя файла). То есть она объединяет работу функций get_book_files и read_book_info."""
    
    books_info = []
    books_list = get_book_files(library_dir)
    for book in books_list:
        book_info = read_book_info(library_dir, book)
        book_info += (book, )
        books_info.append(book_info)
    return books_info

