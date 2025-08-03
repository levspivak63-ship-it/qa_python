from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #1)Проверка ,что у добавленной книги нет жанра
    def test_add_new_book_one_book_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert collector.books_genre['Что делать, если ваш кот хочет вас убить'] == ''

    #2)Проверка на добавления дубликата книги
    def test_add_duplicate_book(self, collector):
        collector.add_new_book('Дубль')
        collector.add_new_book('Дубль')
        assert len(collector.books_genre) == 1

    #3)Добавление книги существующего жанра 
    def test_set_valid_genre(self, collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'

    #4)Добавление книги несуществующего жанра
    def test_set_invalid_genre(self, collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Несуществующий жанр')
        assert collector.get_book_genre('Книга') == ''

    #5)Проверка  ,что по имени можно получить жанр
    def test_get_book_genre_one_book_got_genre(self, collector):
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Фантастика')
        assert collector.get_book_genre('Чужой') == 'Фантастика'

    #6)Проверка вывода списка книг определенного жанра
    def test_get_books_with_specific_genre_two_horror_book(self):
        collector = BooksCollector()
        collector.add_new_book('Ромео и Джульетта')
        collector.set_book_genre('Ромео и Джульетта', 'Трагедии')
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Фантастика')
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == ['1984', 'Чужой']

    #7)Проверка вывода книг подходящих детям
    def test_get_children_books(self, collector):
        collector.add_new_book('Король лев')
        collector.add_new_book('Чужой')
        collector.set_book_genre('Король лев', 'Мультфильмы')
        collector.set_book_genre('Чужой', 'Фантастика')
        children_books = collector.get_books_for_children()
        assert 'Мультфильмы' in children_books
        assert 'Фантастика' not in children_books 

    #8)Проверка добавления книги в избранное
    def test_add_to_favorites(self, collector):
        collector.add_new_book('Чужой')
        collector.add_book_in_favorites('Чужой')
        assert 'Чужой' in collector.get_list_of_favorites_books()

    #9)Проверка двойного добавления книги в избранное
    def test_add_to_favorites_twice(self, collector):
        collector.add_new_book('Чужой')
        collector.add_book_in_favorites('Чужой')
        collector.add_book_in_favorites('Чужой')
        assert len(collector.get_list_of_favorites_books()) == 1 

    #10)Проверка удаления из избранного
    def test_remove_from_favorites(self, collector):
        collector.add_new_book('Чужой')
        collector.add_book_in_favorites('Чужой')
        collector.delete_book_from_favorites('Чужой')
        assert 'Книга' not in collector.get_list_of_favorites_books() 

    #11)Проверка вывода списка избранного
    def test_get_list_of_favorites_books_got_list(self):
        collector = BooksCollector()
        collector.add_new_book('Ромео и Джульетта')
        collector.add_new_book('Чужой')
        collector.add_new_book('1984')
        collector.add_book_in_favorites('Чужой')
        collector.add_book_in_favorites('1984')
        assert collector.get_list_of_favorites_books() == ['Чужой', '1984']  

