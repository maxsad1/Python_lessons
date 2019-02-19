from django.shortcuts import render
from datetime import datetime
from random import randint
from django.conf import settings

from hello import library_dir
# Create your views here.

LIBRARY = settings.LIBRARY

def main(request):
    descr = library_dir.read_library_description(LIBRARY)
    books_info = library_dir.get_all_books_info(LIBRARY)
    authors = library_dir.get_authors(LIBRARY)

    # books_dict = []
    # for (author, title, annot, filename) in books_info:
    #     book = {
    #         'author': author,
    #         'title': title,
    #         'annot': annot,
    #         'file': filename
    #     }
    #     books_dict.append(book)

    data = []
    for author in authors:
        auth_data = {
            'author': author,
            'books': []
        }
        books = []
        for info in books_info:
            (info_author, info__title, _, info_file) = info
            if author == info_author:
                book = {
                    'title': info__title,
                    'file': info_file
                }
            books.append(book)
        auth_data['books'] = books
        data.append(auth_data)
    context = {
        'descr': descr,
        'authors': data
    }
    return render(request, 'main.html', context)
