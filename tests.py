import pytest
from main import BooksCollector

class TestBooksCollector:
    @pytest.fixture
    def collector(self):
        return BooksCollector()
    
    @pytest.fixture
    def collector_with_books(self):

        collector = BooksCollector()  
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.set_book_genre("Книга 2", "Комедии")
        collector.add_book_in_favorites("Книга 1")
        return collector

    def test_add_new_book_valid_name(self, collector):
        collector.add_new_book('Том Сойер')
        assert 'Том Сойер' in collector.get_books_genre()

    def test_add_new_book_invalid_name_too_short(self, collector):
        collector.add_new_book('')
        assert '' not in collector.get_books_genre()

    def test_add_new_book_invalid_name_too_long(self, collector):
        long_name = 'x' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book('Том Сойер')
        collector.add_new_book('Том Сойер')
        assert len(collector.get_books_genre()) == 1

    def test_added_book_has_no_genre(self, collector):
        collector.add_new_book('Том Сойер')
        assert collector.get_book_genre('Том Сойер') == ''

    def test_set_book_genre_valid(self, collector):
        collector.add_new_book('Том Сойер')
        collector.set_book_genre('Том Сойер', 'Фантастика')
        assert collector.get_book_genre('Том Сойер') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book('Том Сойер')
        collector.set_book_genre('Том Сойер', 'Фэнтези')
        assert collector.get_book_genre('Том Сойер') == ''

    def test_set_book_genre_nonexistent_book(self, collector):
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_books_with_specific_genre(self, collector_with_books):
        books = collector_with_books.get_books_with_specific_genre('Фантастика')
        assert 'Книга 1' in books
        assert len(books) == 1

    def test_get_books_for_children(self, collector_with_books):
        children_books = collector_with_books.get_books_for_children()
        assert 'Книга 1' in children_books  
        assert 'Книга 2' in children_books  
        assert len(children_books) == 2

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Том Сойер')
        collector.add_book_in_favorites('Том Сойер')
        assert 'Том Сойер' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self, collector):
        collector.add_new_book('Том Сойер')
        collector.add_book_in_favorites('Том Сойер')
        collector.add_book_in_favorites('Том Сойер')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self, collector_with_books):
        collector_with_books.delete_book_from_favorites("Книга 1")
        assert "Книга 1" not in collector_with_books.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector_with_books):
        favorites = collector_with_books.get_list_of_favorites_books()
        assert 'Книга 1' in favorites
        assert len(favorites) == 1