import library_dir

library = 'library'
content = read_library_description(library)
print(content)

book_list = get_book_files(library)
print(book_list)

book_file = 'O_narodnom_vospitanii.txt'
book_info = read_book_info(library, book_file)
print(book_info)

authors = get_authors(library)
print(authors)

books_info = get_all_books_info(library)
print(books_info)
