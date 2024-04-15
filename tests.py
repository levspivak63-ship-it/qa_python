from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': '',
                                         'Что делать, если ваш кот хочет вас убить': ''}

    def test_add_new_book_too_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('Клуб любителей книг и пирогов из картофельных очистков')
        assert collector.get_books_genre() == {}

    def test_set_book_genre_to_one_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Происхождение')
        collector.set_book_genre('Происхождение', 'Детективы')
        assert collector.get_books_genre().get('Происхождение') == 'Детективы'

    def test_get_book_genre_existing_book(self, book_collector):
        assert book_collector.get_book_genre('Двенадцать стульев') == 'Комедии'

    def test_get_books_with_specific_genre_books_from_existing_dict(self, book_collector):
        assert book_collector.get_books_with_specific_genre('Комедии') == ['Ревизор',
                                                                      'Двенадцать стульев',
                                                                      'Золотой теленок']

    def test_get_books_genre_books_from_existing_dict(self, book_collector):
        assert book_collector.get_books_genre() == {'Дом огней': 'Детективы',
                                                    'Космический десант': 'Фантастика',
                                                    'Ревизор': 'Комедии',
                                                    'Двенадцать стульев': 'Комедии',
                                                    'Золотой теленок': 'Комедии',
                                                    'Сияние': 'Ужасы'
                                                    }

    def test_get_books_for_children_exist_books_for_children_in_dict(self, book_collector):
        assert book_collector.get_books_for_children() == ['Космический десант',
                                                           'Ревизор',
                                                           'Двенадцать стульев',
                                                           'Золотой теленок']

    def test_add_book_in_favorites_add_one_book_from_existing_dict(self, book_collector):
        book_collector.add_book_in_favorites('Двенадцать стульев')
        assert book_collector.get_list_of_favorites_books() == ['Двенадцать стульев']

    def test_add_book_in_favorites_add_one_book_not_from_dict(self, book_collector):
        book_collector.add_book_in_favorites('Призрак оперы')
        assert book_collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_book_already_in_favorites(self, favorite_books):
        collector = BooksCollector()
        collector.favorites = favorite_books
        collector.add_book_in_favorites('Дом огней')
        assert collector.get_list_of_favorites_books() == ['Сияние', 'Серебряные облака', 'Дом огней']

    def test_delete_book_from_favorites_book_from_favorites(self, favorite_books):
        collector = BooksCollector()
        collector.favorites = favorite_books
        collector.delete_book_from_favorites('Дом огней')
        assert collector.get_list_of_favorites_books() == ['Сияние', 'Серебряные облака']

    def test_get_list_of_favorites_books_existing_favorite_list(self, favorite_books):
        collector = BooksCollector()
        collector.favorites = favorite_books
        assert collector.get_list_of_favorites_books() == ['Сияние', 'Серебряные облака', 'Дом огней']