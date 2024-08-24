import pytest
from main import BooksCollector


class TestBooksCollector:

    # Позитивный тест для метода __init__
    def test_all_genres_true(self):
        books_collector = BooksCollector()
        assert books_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    # Позитивный тест для метода add_new_book
    def test_add_new_book_correct_dict(self):
        books_collector = BooksCollector()
        book_name = 'The Great Gatsby'

        books_collector.add_new_book(book_name)

        assert books_collector.books_genre[book_name] == ''

    # Первый негативный тест для метода add_new_book
    @pytest.mark.parametrize('book_name', ['', 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'])
    def test_add_new_book_length_more_than40_or_equal_zero_empty_list(self, book_name):
        books_collector = BooksCollector()
        books_collector.add_new_book(book_name)

        assert len(books_collector.books_genre) == 0

    # Второй негативный тест для метода add_new_book
    @pytest.mark.parametrize('book_name', ['The Great Gatsby', 'In Search of Lost Time'])
    def test_add_new_book_repeating_book_name_twice(self, book_name):
        books_collector = BooksCollector()
        books_collector.add_new_book(book_name)
        books_collector.add_new_book(book_name)

        assert len(books_collector.books_genre) == 1

    # Позитивный тест для метода set_book_genre
    def test_set_book_genre_existing_book_name_and_existing_genre(self):
        books_collector = BooksCollector()
        book_name = 'Thornhedge'
        book_genre = 'Фантастика'

        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, book_genre)

        assert books_collector.books_genre[book_name] == book_genre

    # Позитивный тест для метода get_book_genre (жанр есть)
    def test_get_book_genre_genre_exist_correct(self):
        books_collector = BooksCollector()
        book_name = 'Thornhedge'
        book_genre = 'Фантастика'

        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, book_genre)

        assert books_collector.get_book_genre(book_name) == book_genre

    # Позитивный тест для метода get_book_genre (жанра нет)
    def test_get_book_genre_genre_do_not_exist_correct(self):
        books_collector = BooksCollector()
        book_name = 'Thornhedge'

        books_collector.add_new_book(book_name)

        assert books_collector.get_book_genre(book_name) == ''

    # Позитивный тест для метода get_books_with_specific_genre
    def test_get_books_with_specific_genre_correct(self):
        books_collector = BooksCollector()
        book_name_1 = 'Thornhedge'
        book_name_2 = 'Divine Rivals'
        book_genre_1 = 'Фантастика'
        book_name_3 = 'Frankenstein'
        book_genre_2 = 'Ужасы'

        books_collector.add_new_book(book_name_1)
        books_collector.add_new_book(book_name_2)
        books_collector.set_book_genre(book_name_1, book_genre_1)
        books_collector.set_book_genre(book_name_2, book_genre_1)
        books_collector.set_book_genre(book_name_3, book_genre_2)

        assert books_collector.get_books_with_specific_genre(book_genre_1) == [book_name_1, book_name_2]

    # Позитивный тест для метода get_books_genre
    def test_get_books_genre_correct(self):
        books_collector = BooksCollector()
        book_name_1 = 'Thornhedge'
        book_genre_1 = 'Фантастика'
        book_name_2 = 'Frankenstein'

        books_collector.add_new_book(book_name_1)
        books_collector.add_new_book(book_name_2)
        books_collector.set_book_genre(book_name_1, book_genre_1)

        assert books_collector.get_books_genre() == {book_name_1: book_genre_1,
                                                     book_name_2: ''}

    # Позитивный тест для метода get_books_for_children
    def test_get_books_for_children_correct(self):
        books_collector = BooksCollector()
        book_name_1 = 'Thornhedge'
        book_genre_1 = 'Фантастика'
        book_name_2 = 'Frankenstein'
        book_genre_2 = 'Ужасы'

        books_collector.add_new_book(book_name_1)
        books_collector.add_new_book(book_name_2)
        books_collector.set_book_genre(book_name_1, book_genre_1)
        books_collector.set_book_genre(book_name_2, book_genre_2)

        assert books_collector.get_books_for_children() == [book_name_1]

    # Позитивный тест для метода add_book_in_favorites
    def test_add_book_in_favorites_correct(self):
        books_collector = BooksCollector()
        book_name_1 = 'Thornhedge'
        book_name_2 = 'Frankenstein'

        books_collector.add_new_book(book_name_1)
        books_collector.add_new_book(book_name_2)
        books_collector.add_book_in_favorites(book_name_2)

        assert books_collector.favorites == [book_name_2]

    # Позитивный тест для метода delete_book_from_favorites
    def test_delete_book_from_favorites_correct(self):
        books_collector = BooksCollector()
        book_name_1 = 'Thornhedge'
        book_name_2 = 'Frankenstein'

        books_collector.add_new_book(book_name_1)
        books_collector.add_new_book(book_name_2)
        books_collector.add_book_in_favorites(book_name_1)
        books_collector.add_book_in_favorites(book_name_2)
        books_collector.delete_book_from_favorites(book_name_2)

        assert books_collector.favorites == [book_name_1]

    # Позитивный тест для метода get_list_of_favorites_books
    def test_get_list_of_favorites_books_correct(self):
        books_collector = BooksCollector()
        book_name_1 = 'Thornhedge'
        book_name_2 = 'Frankenstein'

        books_collector.add_new_book(book_name_1)
        books_collector.add_new_book(book_name_2)
        books_collector.add_book_in_favorites(book_name_1)
        books_collector.add_book_in_favorites(book_name_2)

        assert books_collector.get_list_of_favorites_books() == [book_name_1, book_name_2]
