import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, books_collection):
        book_name_1 = 'Гордость и предубеждение и зомби'
        book_name_2 = 'Что делать, если ваш кот хочет вас убить'
        books_collection.add_new_book(book_name_1)
        books_collection.add_new_book(book_name_2)
        assert books_collection.get_books_genre() == {book_name_1: '', book_name_2: ''}

    def test_add_new_book_already_added_book(self, books_collection):
        book_name = 'Гордость и предубеждение'
        books_collection.add_new_book(book_name)
        books_collection.add_new_book(book_name)
        assert len(books_collection.get_books_genre()) == 1

    in_the_range_book_names =['К югу от границы',
                        'Любовь как роза, красива, но шипы больны',
                        'Я']
    @pytest.mark.parametrize('name', in_the_range_book_names)
    def test_add_new_book_name_in_the_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert name in books_collection.get_books_genre()

    out_of_range_book_names = ['',
                          'Удивительное путешествие Нильса Хольгерсс',
                          'Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции']

    @pytest.mark.parametrize('name', out_of_range_book_names)
    def test_add_new_book_name_out_of_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert name not in books_collection.get_books_genre()

    def test_set_book_genre_to_existing_book(self, books_collection):
        book_name = 'Гордость и предубеждение'
        book_genre = 'Фантастика'
        books_collection.add_new_book(book_name)
        books_collection.set_book_genre(book_name, book_genre)
        assert books_collection.get_books_genre() == {book_name: book_genre}

    def test_set_book_genre_to_not_existing_book(self, books_collection):
        book_name = 'Гордость и предубеждение'
        book_genre = 'Фантастика'
        books_collection.set_book_genre(book_name, book_genre)
        assert len(books_collection.get_books_genre()) == 0

    def test_set_book_genre_to_not_existing_genre(self, books_collection):
        book_name = 'Гордость и предубеждение'
        book_genre = 'Трагикомедии'
        books_collection.add_new_book(book_name)
        books_collection.set_book_genre(book_name, book_genre)
        assert books_collection.get_books_genre()[book_name] == ''

    @pytest.mark.parametrize('name, genre', [('Гордость и предубеждение и зомби', 'Ужасы'),
                                             ('Что делать, если ваш кот хочет вас убить', 'Комедии')])
    def test_get_book_genre_by_name(self, name, genre, books_collection):
        books_collection.add_new_book(name)
        books_collection.set_book_genre(name, genre)
        assert books_collection.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_by_genre(self, comedy_and_horror_collection):
        books = comedy_and_horror_collection.get_books_genre()
        first_book_name = list(books.keys())[0]
        first_book_genre = books[first_book_name]

        assert comedy_and_horror_collection.get_books_with_specific_genre(first_book_genre) == [first_book_name]

    def test_get_books_with_specific_genre_for_not_existing_genre(self, comedy_and_horror_collection):
        assert comedy_and_horror_collection.get_books_with_specific_genre('Мультфильмы') == []

    def test_get_books_with_specific_genre_by_wrong_genre(self, comedy_and_horror_collection):
        assert len(comedy_and_horror_collection.get_books_with_specific_genre('Трагикомедии')) == 0

    def test_get_books_for_children(self, adult_collection):
        book_for_child = 'Гадкий Я'
        book_genre_for_child  = 'Мультфильмы'
        adult_collection.add_new_book(book_for_child)
        adult_collection.set_book_genre(book_for_child, book_genre_for_child)
        
        assert len(adult_collection.get_books_for_children()) == 1
        assert adult_collection.get_books_for_children() == ['Гадкий Я']

    def test_add_book_in_favorites_added_in_favorites_book(self, comedy_and_horror_collection):
        first_book_name = list(comedy_and_horror_collection.get_books_genre().keys())[0]

        comedy_and_horror_collection.add_book_in_favorites(first_book_name)
        assert first_book_name in comedy_and_horror_collection.get_list_of_favorites_books()
        assert len(comedy_and_horror_collection.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_for_not_existing_book(self, books_collection):
        book_name_1 = 'Что делать, если ваш кот хочет вас убить'
        book_genre_1  = 'Комедии'
        books_collection.add_new_book(book_name_1)
        books_collection.set_book_genre(book_name_1, book_genre_1)

        books_collection.add_book_in_favorites('Симбиоз')
        assert len(books_collection.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites(self, books_collection):
        book_name_1 = 'Что делать, если ваш кот хочет вас убить'
        book_genre_1  = 'Комедии'
        books_collection.add_new_book(book_name_1)
        books_collection.set_book_genre(book_name_1, book_genre_1)
        books_collection.add_book_in_favorites(book_name_1)
        favorites_book_count_before = len(books_collection.get_list_of_favorites_books())

        books_collection.delete_book_from_favorites(book_name_1)
        assert favorites_book_count_before == 1
        assert len(books_collection.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_for_not_favorites_book(self, comedy_and_horror_collection):
        first_book_name = list(comedy_and_horror_collection.get_books_genre().keys())[0]
        second_book_name = list(comedy_and_horror_collection.get_books_genre().keys())[1]

        comedy_and_horror_collection.add_book_in_favorites(first_book_name)

        comedy_and_horror_collection.delete_book_from_favorites(second_book_name)
        assert len(comedy_and_horror_collection.get_list_of_favorites_books()) == 1
        assert comedy_and_horror_collection.get_list_of_favorites_books() == [first_book_name]
