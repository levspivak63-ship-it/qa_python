import pytest
from main import BooksCollector
from data import BOOKS_DATA


@pytest.fixture
def collector_with_books():
    collector = BooksCollector()
    for name, genre in BOOKS_DATA:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector
