import pytest
from main import BooksCollector
from data import BOOKS_DATA


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()

        collector.add_new_book('')

        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_41_symbol_name(self):
        collector = BooksCollector()
        name = 'B' * 41

        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('name, genre', BOOKS_DATA)
    def test_set_book_genre_set_six_genre(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)

        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    def test_get_book_genre_return_added_genre(self, collector_with_books):
        collector = collector_with_books

        assert collector.get_book_genre('Лабиринт будущего') == 'Фантастика'
        assert collector.get_book_genre('Приключения плюшевого мишки') == 'Мультфильмы'

    @pytest.mark.parametrize('name, genre', BOOKS_DATA)
    def test_get_books_with_specific_genre_six_genre(self, name, genre, collector_with_books):
        collector = collector_with_books

        books = collector.get_books_with_specific_genre(genre)

        assert len(books) == 1 and books[0] == name

    def test_get_books_genre_return_dict(self, collector_with_books):
        collector = collector_with_books
        data_dict = {
            "Тень за стеной": "Ужасы",
            "Лабиринт будущего": "Фантастика",
            "Улика в тумане": "Детективы",
            "Смех в мультивселенной": "Комедии",
            "Приключения плюшевого мишки": "Мультфильмы"
        }

        assert collector.get_books_genre() == data_dict

    def test_get_books_for_children_get_list(self, collector_with_books):
        collector = collector_with_books

        list_books = collector.get_books_for_children()

        assert set(list_books) == {'Лабиринт будущего', 'Смех в мультивселенной', 'Приключения плюшевого мишки'}

    def test_add_book_in_favorites_add_two_books(self, collector_with_books):
        first_book = 'Тень за стеной'
        second_book = 'Приключения плюшевого мишки'
        collector = collector_with_books

        collector.add_book_in_favorites(first_book)
        collector.add_book_in_favorites(second_book)

        list_favorite_books = collector.get_list_of_favorites_books()

        assert set(list_favorite_books) == {first_book, second_book}

    def test_delete_book_from_favorites_add_two_books_delete_one(self, collector_with_books):
        first_book = 'Тень за стеной'
        second_book = 'Приключения плюшевого мишки'
        collector = collector_with_books

        collector.add_book_in_favorites(first_book)
        collector.add_book_in_favorites(second_book)

        collector.delete_book_from_favorites(first_book)

        favorite_book = collector.get_list_of_favorites_books()

        assert favorite_book == [second_book]

    def test_delete_book_from_favorites_deleted_book_not_in_list(self, collector_with_books):
        first_book = 'Тень за стеной'
        second_book = 'Приключения плюшевого мишки'
        collector = collector_with_books

        collector.add_book_in_favorites(first_book)
        collector.add_book_in_favorites(second_book)

        collector.delete_book_from_favorites('Смех в мультивселенной')

        list_favorite_books = collector.get_list_of_favorites_books()

        assert set(list_favorite_books) == {first_book, second_book}

    def test_get_list_of_favorites_books_return_added_books(self, collector_with_books):
        first_book = 'Улика в тумане'
        second_book = 'Смех в мультивселенной'
        collector = collector_with_books

        collector.add_book_in_favorites(first_book)
        assert collector.get_list_of_favorites_books() == [first_book]

        collector.add_book_in_favorites(second_book)
        assert set(collector.get_list_of_favorites_books()) == {first_book, second_book}

    def test_get_list_of_favorites_books_returns_empty_list(self, collector_with_books):
        collector = collector_with_books

        assert collector.get_list_of_favorites_books() == []
