from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


        
# параметризированный тест: проверка добавления новых книг 

import pytest 

class TestBooksCollector:
    # передаем параметры в декратор в виде списка списков  
    @pytest.mark.parametrize("book_name, expected_result", [
    ("Академия", True),                      # название книги с количеством символов < 40 - положительный результат
    ("", False),                          # пустое название книги — отрицательный результат
    ("X" * 50, False),                      # слишком длинное название - отрицательный результат
    ("Академия", False),                    # дубликат книги — отрицательный результат
    ("X", True),                            # название из  одного символа - положительный результат
    ("X" * 40, True),                    # длина ровно 40 символов — положительный результат
    ("X" * 41, False)                   # длина 41 — отрицательный результат
])

    def test_add_new_book(book_name, expected_result):
        collector = BooksCollector()
    # проверка добавления дубликата книги "Академия"
        if expected_result is False and book_name == "Академия":
            collector.add_new_book("Академия") 

        result = collector.add_new_book(book_name)
        assert result == expected_result
        if result:
        # проверка добавления книги в словарь
            assert book_name in collector.books_genre
            
        else:
        # Если не добавили, книги в словаре нет
            assert book_name not in collector.books_genre  == ''

class TestBooksCollector:

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

    # проверка получения списка Избранного
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        
    # добавляем книгу
        collector.add_new_book('Академия')
                
        collector.add_book_in_favorites('Академия')
    # проверяем наличие книги в Избранном
        assert 'Академия' in collector.favorites