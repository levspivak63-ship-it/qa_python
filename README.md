# qa_python
Разработан в рамках обучения на курсе ЯП "Инженер по тестированию: от новичка до автоматизатора". Суть проекта покрыть тестами приложение BooksCollector, которое позволяет установить жанр книг и добавить их в избранное. Автоматизировано юнит-тестирование с помощью фикстур и параметризации.

Запустить проект можно с помощью команды в терминале: pytest tests.py -v

Реализованы фикстуры:
  1. books_collection: возвращает объект класса BooksCollector
  2. comedy_and_horror_collection: возвращает коллекцию с двумя книгами (ужасы и комедии)
  3. adult_collection: возвращает коллекцию с одной книгой жанра "Ужасы"

Сценарии, покрытые тестами:
  1. test_add_new_book_add_two_books: проверка добавления двух книг
  2. test_add_new_book_already_added_book: негативная проверка на повторное добавление книги
  3. test_add_new_book_name_in_the_range: параметризованная проверка на добавление книги с валидным названием (3 варианта)
  4. test_add_new_book_name_out_of_range: параметризованная негативная проверка на добавление книги с невалидным названием (3 варианта)
  5. test_set_book_genre_to_existing_book: проверка на добавление жанра из genre для книги из books_genre
  6. test_set_book_genre_to_not_existing_book: негативная проверка на добавление жанра для несуществующей книги
  7. test_set_book_genre_to_not_existing_genre: негативная проверка на добавление жанра НЕ из genre для существующей книги
  8. test_get_book_genre_by_name: параметризованная проверка на вывод жанра книги по ее имени (2 варианта)
  9. test_get_books_with_specific_genre_by_genre: проверка на вывод книг по жанру
  10. test_get_books_with_specific_genre_for_not_existing_genre: негативная проверка на вывод книг по несуществующему жанру
  11. test_get_books_with_specific_genre_by_wrong_genre: негативная проверка на вывод книг по жанру НЕ из genre
  12. test_get_books_for_children: проверка на вывод детских книг
  13. test_add_book_in_favorites_added_in_favorites_book: проверка на добавление книги в избранное
  14. test_add_book_in_favorites_for_not_existing_book: негативная проверка на добавление в избранное несуществующей книги
  15. test_delete_book_from_favorites: проверка на удаление книги из избранного
  16. test_delete_book_from_favorites_for_not_favorites_book: негативная проверка на удаление из избранного книги НЕ добавленной в избранное