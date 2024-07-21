import unittest
from library import Library, Book
import os


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library("test_books.json")

    def tearDown(self):
        if os.path.exists("test_books.json"):
            os.remove("test_books.json")

    def test_add_book(self):
        self.library.add_book("Test Book", "Test Author", "2024")
        books = self.library.load_data()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Test Book")

    def test_remove_book(self):
        self.library.add_book("Test Book", "Test Author", "2024")
        self.library.remove_book(1)
        books = self.library.load_data()
        self.assertEqual(len(books), 0)

    def test_search_books(self):
        self.library.add_book("Test Book", "Test Author", "2024")
        results = self.library.search_books("названию", "Test Book")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Test Book")

    def test_list_books(self):
        self.library.add_book("Test Book", "Test Author", "2024")
        books = self.library.list_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Test Book")

    def test_change_status(self):
        self.library.add_book("Test Book", "Test Author", "2024")
        self.library.change_status(1, "выдана")
