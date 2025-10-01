import pytest
from main import BooksCollector

@pytest.fixture
def books_collection() :
    return BooksCollector()

@pytest.fixture
def comedy_and_horror_collection() :
    collector = BooksCollector()    
    book_name_1 = 'Гордость и предубеждение и зомби'
    book_genre_1  = 'Ужасы'
    book_name_2 = 'Что делать, если ваш кот хочет вас убить'
    book_genre_2  = 'Комедии'
    collector.add_new_book(book_name_1)
    collector.set_book_genre(book_name_1, book_genre_1)
    collector.add_new_book(book_name_2)
    collector.set_book_genre(book_name_2, book_genre_2)

    return collector

@pytest.fixture
def adult_collection() :
    collector = BooksCollector()    
    book_name_1 = 'Гордость и предубеждение и зомби'
    book_genre_1  = 'Ужасы'
    collector.add_new_book(book_name_1)
    collector.set_book_genre(book_name_1, book_genre_1)

    return collector