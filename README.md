Проведены следующие проверки приложения BooksCollector:
- проверки метода add_new_book:
        * добавления новых книг 
        * отказа в добавлении книги с количеством символов в  названии >= 41 
- проверки метода set_book_genre:
        * проверка установки книге жанра из находящихся в списке жанров
        * проверка невозможности установки книге жанра отсутствующего в списке жанров
        * проверка невозможности установки жанра находящихся в списке жанров книге, отсутсвующей в библиотеке
- проверка метода get_book_genre
- проверка метода get_books_with_specific_genre
- проверка вывода текущего словаря books_genre методом get_books_genre
- проверка метода  get_books_for_children:
        * проверка включения в список детских книг книги жанра не находящегося в списке genre_age_rating
        * проверка невключения в список детских книг книги жанра находящегося в списке genre_age_rating
- проверка метода add_book_in_favorites:
        * добавление новой книги в Избранное
        * невозможность добавить повторно книгу в избранное
- проверка метода delete_book_from_favorites
- проверка метода get_list_of_favorites_books

Всего выполнено 14 тестов. Все результаты тестов - положительные.
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0 -- C:\Users\lspiv\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lspiv\yandex\pytest\qa_python
plugins: cov-7.0.0
collected 14 items

tests.py::TestBooksCollector::test_add_new_book_add_two_books PASSED                                                                     [  7%]
tests.py::TestBooksCollector::test__add_new_book_add_48_len PASSED                                                                       [ 14%]
tests.py::TestBooksCollector::test_set_book_genre_book_name_in_books_genre_and_genre_in_genre PASSED                                     [ 21%]
tests.py::TestBooksCollector::test_set_book_genre_book_name_in_books_genre_and_genre_not_in_genre PASSED                                 [ 28%]
tests.py::TestBooksCollector::test_set_book_genre_book_name_not_in_books_genre_and_genre_in_genre PASSED                                 [ 35%]
tests.py::TestBooksCollector::test_get_book_genre_book_and_genre_in_books_genre PASSED                                                   [ 42%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_book_in_books_genre PASSED                                              [ 50%]
tests.py::TestBooksCollector::test_get_books_genre PASSED                                                                                [ 57%]
tests.py::TestBooksCollector::test_get_books_for_children_rating_not_in_genre_age_rating PASSED                                          [ 64%]
tests.py::TestBooksCollector::test_get_books_for_children_in_genre_age_rating PASSED                                                     [ 71%]
tests.py::TestBooksCollector::test_add_book_in_favorites_new PASSED                                                                      [ 78%]
tests.py::TestBooksCollector::test_add_book_in_favorites_already_added PASSED                                                            [ 85%]
tests.py::TestBooksCollector::test_delete_book_from_favorites PASSED                                                                     [ 92%]
tests.py::TestBooksCollector::test_get_list_of_favorites_books PASSED                      python