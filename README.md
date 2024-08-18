import unittest


class TestBooksCollector(unittest.TestCase):

    def setUp(self):
        self.collector = BooksCollector()

    def test_add_new_book(self):
        self.collector.add_new_book("The Great Gatsby")
        self.assertIn("The Great Gatsby", self.collector.books_genre)
        self.assertEqual(self.collector.books_genre["The Great Gatsby"], "")

    def test_add_new_book_invalid_length(self):
        self.collector.add_new_book("")  # Empty name
        self.collector.add_new_book("A" * 41)  # Exceeds 40 characters
        self.assertEqual(len(self.collector.books_genre), 0)

    def test_set_book_genre(self):
        self.collector.add_new_book("Brave New World")
        self.collector.set_book_genre("Brave New World", "Фантастика")
        self.assertEqual(self.collector.books_genre["Brave New World"], "Фантастика")

    def test_set_book_genre_invalid_book(self):
        self.collector.set_book_genre("Nonexistent Book", "Фантастика")
        self.assertEqual(len(self.collector.books_genre), 0)  # No books should be set

    def test_set_book_genre_invalid_genre(self):
        self.collector.add_new_book("The Catcher in the Rye")
        self.collector.set_book_genre("The Catcher in the Rye", "Nonexistent Genre")
        self.assertEqual(self.collector.books_genre["The Catcher in the Rye"], "")

    def test_get_book_genre(self):
        self.collector.add_new_book("Moby Dick")
        self.collector.set_book_genre("Moby Dick", "Фантастика")
        self.assertEqual(self.collector.get_book_genre("Moby Dick"), "Фантастика")

    def test_get_books_genre(self):
        self.collector.add_new_book("Fahrenheit 451")
        self.collector.set_book_genre("Fahrenheit 451", "Фантастика")
        self.assertEqual(self.collector.get_books_genre(), {"Fahrenheit 451": "Фантастика"})

    def test_get_books_for_children(self):
        self.collector.add_new_book("Finding Nemo")
        self.collector.set_book_genre("Finding Nemo", "Мультфильмы")
        self.collector.add_new_book("It")
        self.collector.set_book_genre("It", "Ужасы")
        self.assertEqual(self.collector.get_books_for_children(), ["Finding Nemo"])

    def test_add_book_in_favorites(self):
        self.collector.add_new_book("To Kill a Mockingbird")
        self.collector.set_book_genre("To Kill a Mockingbird", "Детективы")
        self.collector.add_book_in_favorites("To Kill a Mockingbird")
        self.assertIn("To Kill a Mockingbird", self.collector.favorites)

    def test_add_book_in_favorites_not_exist(self):
        self.collector.add_book_in_favorites("Not Exist Book")
        self.assertNotIn("Not Exist Book", self.collector.favorites)


    def test_delete_book_from_favorites(self):
        self.collector.add_new_book("The Lord of the Rings")
        self.collector.set_book_genre("The Lord of the Rings", "Фантастика")
        self.collector.add_book_in_favorites("The Lord of the Rings")
        self.collector.delete_book_from_favorites("The Lord of the Rings")
        self.assertNotIn("The Lord of the Rings", self.collector.favorites)


if __name__ == "__main__":
    unittest.main()
