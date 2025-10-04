from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


        
# параметризированный тест: проверка добавления новых книг 

import pytest 

class TestBooksCollector:
    # передаем параметры в декратор в виде списка списков  
    @pytest.mark.parametrize('book_name, expected_result', [
        # Валидные длины (должны быть добавлены)
        ('A', True),           # 1 символ - минимальная валидная длина
        ('A * 5', True),       # 5 символов
        ('A' * 39, True),      # 39 символов
        ('A' * 40, True),      # 40 символов - максимальная валидная длина
        
        # Невалидные длины (не должны быть добавлены)
        ('', False),           # 0 символов - пустая строка
        ('A' * 41, False),     # 41 символ - превышает максимальную длину
        ('A' * 50, False),     # 50 символов
    ])

    def test_add_new_book_by_length(self, book_name, expected_result):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        # Проверяем результат в зависимости от ожидаемого поведения
        if expected_result:
            # Книга должна быть добавлена
            assert book_name in collector.books_genre
            
        else:
            # Книга не должна быть добавлена
            assert book_name not in collector.books_genre

    # проверка невключения в словарь дубликата
    def test_not_add_duplicate_book(self):
        collector = BooksCollector()
    # добавляем книгу
        collector.add_new_book("Академия")
        assert "Академия" in collector.books_genre
    # Второй раз пытаемся добавить ту же книгу
        collector.add_new_book("Академия")
    # проверяем, что есть только одна запись    
        assert len(collector.books_genre) == 1


        # проверка установки книге жанра из находящихся в списке жанров
    def test_set_book_genre_book_name_in_books_genre_and_genre_in_genre(self):
        collector = BooksCollector()
        # добавляем новую книгу  и устанавливаем жанр
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        # проверяем установку жанра
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

        # проверка невозможности установки книге жанра отсутствующего в списке жанров
    def test_set_book_genre_book_name_in_books_genre_and_genre_not_in_genre(self):
        collector = BooksCollector()
        genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        # добавляем новую книгу  и устанавливаем жанр, отсутсвущий в списке
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Драмма')
        # проверяем отказ установки жанра
        assert collector.get_book_genre('Гордость и предубеждение и зомби') not in genre
   
        # проверка невозможности установки жанра находящихся в списке жанров книге, отсутсвующей в библиотеке
    def test_set_book_genre_book_name_not_in_books_genre_and_genre_in_genre(self):
        collector = BooksCollector()
        # добавляем новую книгу  и устанавливаем жанр другой книге
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('12345', 'Ужасы')
        # проверяем отказ установки жанра
        assert collector.get_book_genre('12345') is None
    
        # проверка получения жанра книги по ее имени
    def test_get_book_genre_book_and_genre_in_books_genre(self):
        collector = BooksCollector()
        # добавляем новую книгу  и устанавливаем жанр
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        # проверяем получение жанра книги по ее имени
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

        # проверка получения из библиотеки списка книг с определенным жанром 
    def test_get_books_with_specific_genre_book_in_books_genre(self):
        collector = BooksCollector()
       # добавляем новую книгу  и устанавливаем жанр
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
       
        # проверяем, что возвращается книга с указанным жанром
        assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби']

        # проверка получения словаря books_genre
    def test_get_books_genre(self):

        # добавляем новую книгу  и устанавливаем жанр
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        # проверяем, что возвращается словарь
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Ужасы'}
    

        # проверка включения в список детских книг книги жанра не находящегося в списке genre_age_rating
    def test_get_books_for_children_rating_not_in_genre_age_rating(self):
        collector = BooksCollector()
       
        # добавляем книгу для детей
        collector.add_new_book('Академия')
        collector.set_book_genre('Академия', 'Фантастика')
        
        # получаем список книг для детей
        books_for_children = collector.get_books_for_children()
        
        # проверка включения в список книги с жанром для детей
        assert 'Академия' in books_for_children
        
            
     # проверка невключения в список детских книг книги жанра находящегося в списке genre_age_rating
    def test_get_books_for_children_in_genre_age_rating(self):
        collector = BooksCollector()
        
        # добавляем книгу для взрослых
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')        

        # получаем список книг для детей
        books_for_children = collector.get_books_for_children()
        
        # проверка невключения в список книги с жанром для взрослых
        assert 'Гордость и предубеждение и зомби' not in books_for_children

    # проверка добавления новой книги в Избранное
    def test_add_book_in_favorites_new(self):
        collector = BooksCollector()
    # добавляем новую книгу
        collector.add_new_book('Академия')
               
        collector.add_book_in_favorites('Академия')
        assert 'Академия' in collector.favorites

    # проверка невозможноти добавить повторно книгу в избранное
    def test_add_book_in_favorites_already_added(self):
        collector = BooksCollector()
    # добавляем новую книгу
        collector.add_new_book('Академия')
        collector.add_book_in_favorites('Академия')
    # добавляем книгу повторно
        collector.add_book_in_favorites('Академия') 

    # проверяем, что в списке только одна книга
        assert len(collector.favorites) == 1      


    # проверка удаляения книги из Избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
    # добавляем книгу
        collector.add_new_book('Академия')
           
    # проверка удаляения книги
        collector.delete_book_from_favorites('Академия')
        assert 'Академия' not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Академия')
        collector.add_new_book('Академия 2')
        # добавляем в избранное
        collector.add_book_in_favorites('Академия')
        collector.add_book_in_favorites('Академия 2')
        # получаем список через метод
        #favorites_books = collector.get_list_of_favorites_books()
        # проверяем, что список содержит нужные книги
        assert collector.get_list_of_favorites_books() == ['Академия', 'Академия 2']