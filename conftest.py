import pytest
from main import BooksCollector


@pytest.fixture
def book_collector():
    book_collector = BooksCollector()
    book_collector.books_genre = {'Дом огней': 'Детективы',
                                  'Космический десант': 'Фантастика',
                                  'Ревизор': 'Комедии',
                                  'Двенадцать стульев': 'Комедии',
                                  'Золотой теленок': 'Комедии',
                                  'Сияние': 'Ужасы'
                                  }
    return book_collector

@pytest.fixture()
def favorite_books():
    book_collector = BooksCollector()
    book_collector.favorites = ['Сияние', 'Серебряные облака', 'Дом огней']
    return book_collector.favorites