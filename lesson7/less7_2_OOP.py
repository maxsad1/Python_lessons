import os

"""
Library                 Book
-------------------     ------------
- описание              - автор
- список книг           - название
- список авторов        - аннотация
-------------------     ------------
- путь к библиотеке     - имя файла
"""

class Library:
    """Class Library

    """
    def __init__(self, lib_dir):
        self._lib_dir = lib_dir
        if not os.path.isdir(self._lib_dir):
            raise NotADirectoryError(f'"{self._lib_dir}" is not a directory')

    def description(self):
        """Read description.txt"""
        desc_file_path = os.path.join(self._lib_dir, 'description.txt')
        try:
            with open(desc_file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return ''
        except PermissionError:
            return ''

    def books(self):
        """List of books"""
        result = []
        for elem in os.scandir(self._lib_dir):
            if elem.is_file():
                if (elem.name.endswith('.txt') and
                    elem.name != 'description.txt'):
                    b = TextBook(elem.path)
                    result.append(b)
                elif(elem.name.endswith('.epub') and
                    elem.name != 'description.txt'):
                    b = EpubBook(elem.path)
                    result.append(b)
        return result

    def authors(self):
        """List of authors"""
        ...


class Book:
    """Class Book

    """
    def __init__(self, filename):
        self._filename = filename
        self._read_info()

    def _read_info(self):
        """Read first three lines of the file"""
        self.author = None
        self.title = None
        self.annotation = None

    def __str__(self):
        return '{}. {}'.format(self.author, self.title)

    def __repr__(self):
        return 'Book({})'.format(repr(self._filename))


class TextBook(Book):
    """Class Text Book

    """
    def __init__(self, filename):
        super().__init__(filename)

    def _read_info(self):
        """Read first three lines of the file"""
        with open(self._filename, 'r', encoding='utf-8') as f:
            self.author = f.readline()[:-1].strip(' .')
            self.title = f.readline()[:-1].strip(' ')
            self.annotation = f.readline()[:-1].strip(' ')


class EpubBook(Book):
    """Class Epub Book

    """
    def __init__(self, filename):
        super().__init__(filename)

    def _read_info(self):
        """Read first three lines of the file"""
        # with open(self._filename, 'r', encoding='utf-8') as f:
        self.author = 'Жюль Верн'
        self.title = 'Таинственный остров'
        self.annotation = 'Таинственный остров'



# lib = Library(r'D:\MyDocs\python\homework\library_dir\library_dir.py')
lib = Library(r'D:\MyDocs\python\homework\library_dir\library')

lib_desc = lib.description()
print(lib_desc)

books_list = lib.books()
print(books_list)

for b in lib.books():
    print(b)