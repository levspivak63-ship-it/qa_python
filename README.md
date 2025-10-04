Проведены следующие проверки приложения BooksCollector:
- параметризированная проверки метода add_new_book добавления новых книг:
        * граничных условий названия, КЭ 
- проверка добавления дубликата выделена в отдельный тест 
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
- исправлена проверка метода get_list_of_favorites_books 

Всего выполнено 20 тестов. Все результаты тестов - положительные.
plugins: cov-7.0.0
collected 20 items

tests.py::TestBooksCollector::test_add_new_book_by_length[A-True] PASSED                                                                 [  5%]
tests.py::TestBooksCollector::test_add_new_book_by_length[A * 5-True] PASSED                                                             [ 10%]
tests.py::TestBooksCollector::test_add_new_book_by_length[AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-True] PASSED                           [ 15%]
tests.py::TestBooksCollector::test_add_new_book_by_length[AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-True] PASSED                          [ 20%] 
tests.py::TestBooksCollector::test_add_new_book_by_length[-False] PASSED                                                                 [ 25%] 
tests.py::TestBooksCollector::test_add_new_book_by_length[AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-False] PASSED                        [ 30%] 
tests.py::TestBooksCollector::test_add_new_book_by_length[AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-False] PASSED               [ 35%] 
tests.py::TestBooksCollector::test_not_add_duplicate_book PASSED                                                                         [ 40%]
tests.py::TestBooksCollector::test_set_book_genre_book_name_in_books_genre_and_genre_in_genre PASSED                                     [ 45%] 
tests.py::TestBooksCollector::test_set_book_genre_book_name_in_books_genre_and_genre_not_in_genre PASSED                                 [ 50%] 
tests.py::TestBooksCollector::test_set_book_genre_book_name_not_in_books_genre_and_genre_in_genre PASSED                                 [ 55%] 
tests.py::TestBooksCollector::test_get_book_genre_book_and_genre_in_books_genre PASSED                                                   [ 60%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_book_in_books_genre PASSED                                              [ 65%] 
tests.py::TestBooksCollector::test_get_books_genre PASSED                                                                                [ 70%] 
tests.py::TestBooksCollector::test_get_books_for_children_rating_not_in_genre_age_rating PASSED                                          [ 75%] 
tests.py::TestBooksCollector::test_get_books_for_children_in_genre_age_rating PASSED                                                     [ 80%] 
tests.py::TestBooksCollector::test_add_book_in_favorites_new PASSED                                                                      [ 85%] 
tests.py::TestBooksCollector::test_add_book_in_favorites_already_added PASSED                                                            [ 90%] 
tests.py::TestBooksCollector::test_delete_book_from_favorites PASSED                                                                     [ 95%] 
tests.py::TestBooksCollector::test_get_list_of_favorites_books PASSED                                                                    [100%] 

