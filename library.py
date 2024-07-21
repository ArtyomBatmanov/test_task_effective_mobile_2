import json
import os
from typing import List, Dict, Union

DATA_FILE = "books.json"


class Book:
    """
    Класс для представления книги.
    """

    def __init__(
        self, id: int, title: str, author: str, year: str, status: str
    ) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __dict__(self) -> Dict[str, Union[int, str]]:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }


class Library:
    """
    Класс для управления библиотекой.
    """

    def __init__(self, data_file: str) -> None:
        self.data_file = data_file

    def load_data(self) -> List[Book]:
        """
        Загружает данные из файла JSON.
        Если файл не существует или пуст, возвращает пустой список.

        Returns:
            List[Book]: Список книг.
        """
        if os.path.exists(self.data_file) and os.path.getsize(self.data_file) > 0:
            with open(self.data_file, "r", encoding="utf-8") as f:
                book_dicts = json.load(f)
                return [Book(**book) for book in book_dicts]
        return []

    def save_data(self, books: List[Book]) -> None:
        """
        Сохраняет данные в файл JSON.

        Args:
            books (List[Book]): Список книг для сохранения.
        """
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(
                [book.__dict__() for book in books], f, indent=4, ensure_ascii=False
            )

    def add_book(self, title: str, author: str, year: str) -> None:
        """
        Добавляет новую книгу в библиотеку.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (str): Год издания книги.
        """
        books = self.load_data()
        new_book = Book(
            id=max([book.id for book in books], default=0) + 1,
            title=title,
            author=author,
            year=year,
            status="в наличии",
        )
        books.append(new_book)
        self.save_data(books)
        print(f"Книга '{title}' успешно добавлена!")

    def remove_book(self, book_id: int) -> None:
        """
        Удаляет книгу из библиотеки по её ID.

        Args:
            book_id (int): ID книги для удаления.
        """
        books = self.load_data()
        book_to_remove = next((book for book in books if book.id == book_id), None)
        if book_to_remove:
            books.remove(book_to_remove)
            self.save_data(books)
            print(f"Книга с ID {book_id} успешно удалена!")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def search_books(self, search_type: str, search_query: str) -> List[Book]:
        """
        Ищет книги в библиотеке по названию, автору или году издания.

        Args:
            search_type (str): Тип поиска ('названию', 'автору', 'году').
            search_query (str): Запрос поиска.

        Returns:
            List[Book]: Список найденных книг.
        """
        books = self.load_data()
        if search_type == "названию":
            results = [
                book for book in books if search_query.lower() in book.title.lower()
            ]
        elif search_type == "автору":
            results = [
                book for book in books if search_query.lower() in book.author.lower()
            ]
        elif search_type == "году":
            results = [book for book in books if book.year == search_query]
        else:
            print("Неверный тип поиска.")
            return []

        return results

    def list_books(self) -> List[Book]:
        """
        Отображает список всех книг в библиотеке.

        Returns:
            List[Book]: Список всех книг.
        """
        return self.load_data()

    def change_status(self, book_id: int, new_status: str) -> None:
        """
        Изменяет статус книги по её ID.

        Args:
            book_id (int): ID книги.
            new_status (str): Новый статус книги ('в наличии' или 'выдана').
        """
        books = self.load_data()
        book_to_change = next((book for book in books if book.id == book_id), None)
        if book_to_change:
            book_to_change.status = new_status
            self.save_data(books)
            print(f"Статус книги с ID {book_id} изменен на '{new_status}' успешно!")
        else:
            print(f"Книга с ID {book_id} не найдена.")
