import pytest
from main import BooksCollector
from data import *


class TestBooksCollector:

    @pytest.mark.parametrize('book_name', BOOKS)
    def test_add_new_book_success(self, collector, book_name):
        collector.add_new_book(book_name)

        assert book_name in collector.get_books_genre()

    def test_add_multiple_books(self, collector):
        for book_name in BOOKS:
            collector.add_new_book(book_name)

            assert book_name in collector.get_books_genre()

    def test_set_book_genre_success_book_is_added(self, collector):
        book_name = '1984'
        genre = 'Детективы'

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.get_book_genre(book_name) == genre

    def test_set_book_genre_book_not_in_genre(self, collector):
        book_name = "Неизвестная книга"
        genre = "Фантастика"

        collector.set_book_genre(book_name, genre)

        assert collector.get_book_genre(book_name) is None

    def test_get_books_for_children(self):
        collector = BooksCollector()

        book_name_for_kids = 'Смешарики'
        book_name_for_adults = 'Астрал'

        collector.add_new_book(book_name_for_kids)
        collector.set_book_genre(book_name_for_kids, 'Мультфильмы')

        collector.add_new_book(book_name_for_adults)
        collector.set_book_genre(book_name_for_adults, 'Ужасы')

        books_for_children = collector.get_books_for_children()

        assert book_name_for_kids in books_for_children
        assert book_name_for_adults not in books_for_children

    def test_add_book_in_favorites(self, collector):
        book_name = '1984'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert book_name in collector.get_list_of_favorites_books()

    def test_add_book_duplicate_not_in_favorites(self, collector):
        book_name = '1984'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)

        assert collector.get_list_of_favorites_books().count(book_name) == 1

    def test_delete_book_from_favorites(self, collector):
        book_name = '1984'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)

        assert book_name not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('book_name, genre', [
        ('Эго - Твой Враг', 'Фантастика'),
        ('Мирный Воин', 'Детективы'),
    ])
    def test_get_books_with_specific_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books_with_genre = collector.get_books_with_specific_genre(genre)
        assert book_name in books_with_genre

    @pytest.mark.parametrize('book_name', BOOKS)
    def test_get_books_genre(self, collector, book_name):
        collector.add_new_book(book_name)
        books_genre = collector.get_books_genre()
        assert book_name in books_genre

    @pytest.mark.parametrize('book_name, genre', [
        ('Эго - Твой Враг', 'Фантастика'),
        ('Мирный Воин', 'Комедии'),
    ])
    def test_get_one_book_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        book_genre = collector.get_book_genre(book_name)
        assert book_genre == genre
