import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Вокруг света за 80 дней')
        collector.add_new_book('Десять негритят')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("name", ["", "A" * 41])
    def test_add_new_book_invalid_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Вокруг света за 80 дней")
        collector.set_book_genre("Вокруг света за 80 дней", "Приключения")
        assert collector.get_book_genre("Вокруг света за 80 дней") == "Приключения"

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Неизвестный жанр")
        assert collector.get_book_genre("Книга") == ""

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Вокруг света за 80 дней")
        collector.set_book_genre("Вокруг света за 80 дней", "Приключения")
        collector.add_new_book("Десять негритят")
        collector.set_book_genre("Десять негритят", "Детективы")
        assert collector.get_books_with_specific_genre("Приключения") == ["Вокруг света за 80 дней"]

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Вокруг света за 80 дней")
        collector.set_book_genre("Вокруг света за 80 дней", "Приключения")
        collector.add_new_book("Десять негритят")
        collector.set_book_genre("Десять негритят", "Детективы")
        assert collector.get_books_for_children() == ["Вокруг света за 80 дней"]

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Вокруг света за 80 дней")
        collector.add_book_in_favorites("Вокруг света за 80 дней")
        assert "Вокруг света за 80 дней" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book("Вокруг света за 80 дней")
        collector.add_book_in_favorites("Вокруг света за 80 дней")
        collector.add_book_in_favorites("Вокруг света за 80 дней")
        assert collector.get_list_of_favorites_books().count("Вокруг света за 80 дней") == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Вокруг света за 80 дней")
        collector.add_book_in_favorites("Вокруг света за 80 дней")
        collector.delete_book_from_favorites("Вокруг света за 80 дней")
        assert "Вокруг света за 80 дней" not in collector.get_list_of_favorites_books()