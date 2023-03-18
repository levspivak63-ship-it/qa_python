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
    def test_add_new_book_new_book_rating_is_1(self):
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 1')
        assert collector.get_book_rating('Книга с рейтингом 1') == 1

    def test_add_new_book_add_two_simmilar_book_added_only_one_book(self):
        """
        Добавление 2х книг с одинаковым названием. Ожидаемый результат: в колекцию книг добавлена только одна книга
        """
        collector = BooksCollector()
        collector.add_new_book('Книга близнец')
        collector.add_new_book('Книга близнец')
        assert len(collector.get_books_rating()) == 1

    def test_get_book_rating_book_doesnt_exist_got_rating_is_none(self):
        """
        Проверка рейтинга недобавленной книги. Ожидаемый результат: None
        """
        collector = BooksCollector()
        assert collector.get_book_rating('Несуществующая книга') is None

    # Тесты для метода set_book_rating
    def test_set_book_rating_rating_0_book_rating_is_1(self):
        """
        Проверка приграничного значения рейтинга. Попытка установить рейтинг = 0. Ожидаемый результат: рейтинг равен 1
        """
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 0')
        collector.set_book_rating('Книга с рейтингом 0', 0)
        assert collector.get_book_rating('Книга с рейтингом 0') == 1

    def test_set_book_rating_rating_1_book_rating_is_1(self):
        """
        Проверка приграничного значения рейтинга. Попытка установить рейтинг = 1. Ожидаемый результат: рейтинг равен 1
        """
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 1')
        collector.set_book_rating('Книга с рейтингом 1', 1)
        assert collector.get_book_rating('Книга с рейтингом 1') == 1

    def test_set_book_rating_rating_2_book_rating_is_2(self):
        """
        Проверка приграничного значения рейтинга. Попытка установить рейтинг = 2. Ожидаемый результат: рейтинг равен 2
        """
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 2')
        collector.set_book_rating('Книга с рейтингом 2', 2)
        assert collector.get_book_rating('Книга с рейтингом 2') == 2

    def test_set_book_rating_rating_9_book_rating_is_9(self):
        """
        Проверка приграничного значения рейтинга. Попытка установить рейтинг = 9. Ожидаемый результат: рейтинг равен 9
        """
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 9')
        collector.set_book_rating('Книга с рейтингом 9', 9)
        assert collector.get_book_rating('Книга с рейтингом 9') == 9

    def test_set_book_rating_rating_10_book_rating_is_10(self):
        """
        Проверка приграничного значения рейтинга. Попытка установить рейтинг = 10. Ожидаемый результат: рейтинг равен 10
        """
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 10')
        collector.set_book_rating('Книга с рейтингом 10', 10)
        assert collector.get_book_rating('Книга с рейтингом 10') == 10

    def test_set_book_rating_set_book_rating_11_book_rating_is_1(self):
        """
        Проверка приграничного значения рейтинга. Попытка установить рейтинг = 11. Ожидаемый результат: рейтинг равен 1
        """
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 11')
        collector.set_book_rating('Книга с рейтингом 11', 11)
        assert collector.get_book_rating('Книга с рейтингом 11') == 1

    def test_set_book_rating_book_doesnt_exist_book_rating_is_None(self):
        """
        Попытка установить рейтинг для несуществующей книги = 4. Ожидаемый результат: None
        """
        collector = BooksCollector()
        collector.set_book_rating('Несуществующая книга', 4)
        assert collector.get_book_rating('Несуществующая книга') is None

    # Тесты для метода get_books_with_specific_rating
    def test_get_books_with_specific_rating_get_books_with_rating_2_return_2_books(self):
        """
        Попытка добавить две книги с рейтингом 2 и одну книгу с рейтингом 1, отобразить список книг с рейтингом 2.
        Ожидаемый результат: Выведен список из двух книг с рейтингом два.
        """
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 2')
        collector.set_book_rating('Книга с рейтингом 2', 2)
        collector.add_new_book('Еще книга с рейтингом 2')
        collector.set_book_rating('Еще книга с рейтингом 2', 2)
        collector.add_new_book('Книга с рейтингом 1')
        result = collector.get_books_with_specific_rating(2)
        assert len(result) == 2 and 'Книга с рейтингом 2' in result and 'Еще книга с рейтингом 2' in result

    def test_get_books_with_specific_rating_rating_doesnt_exist_return_empty_list(self):
        """
        Попытка найти книги с несуществующим рейтингом. Ожидаемый результат: пустой список
        """
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 1')
        assert len(collector.get_books_with_specific_rating(2)) == 0

    # Тесты для методов add_book_in_favorites + get_list_of_favorites_books
    def test_get_list_of_favorites_books_empty_favorites_books_list_return_empty_list(self):
        """
        Проверка вызова метода get_list_of_favorites_books без добавленных книг. Ожидаемый результат: пустой список
        """
        collector = BooksCollector()
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_add_book_in_favorites_return_one_book(self):
        """
        Проверка вызова метода get_list_of_favorites_books c добавленной книгой. Ожидаемый результат: вернет список
        с добавленной книгой
        """
        collector = BooksCollector()
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        assert collector.get_list_of_favorites_books() == ['Любимая книга']

    def test_add_book_in_favorites_add_nonexistent_book_favorite_books_list_empty(self):
        """
        Попытка добавить книгу в список favorites, если её нет в словаре books_rating. Ожидаемый результат: пустой список
        get_list_of_favorites_books
        """
        collector = BooksCollector()
        collector.add_book_in_favorites('Любимая книга, которой нет в списке')
        assert len(collector.get_list_of_favorites_books()) == 0

    # Тесты метода delete_book_from_favorites
    def test_delete_book_from_favorites_add_and_delete_book_from_favorites_empty_favorite_list(self):
        """
        Попытка добавить книгу в favorites и удалить её. Ожидаемый результат: пустой список get_list_of_favorites_books
        """
        collector = BooksCollector()
        collector.add_new_book('Книга для удаления из фаворитных')
        collector.add_book_in_favorites('Книга для удаления из фаворитных')
        collector.delete_book_from_favorites('Книга для удаления из фаворитных')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_delete_nonexist_book_from_favorites_empty_favorite_list(self):
        """
        Попытка удаалить книгу, не существующую в favorites. Ожидаемый результат: пустой get_list_of_favorites_books
        """
        collector = BooksCollector()
        collector.delete_book_from_favorites('Книга для удаления из фаворитных')
        assert len(collector.get_list_of_favorites_books()) == 0
