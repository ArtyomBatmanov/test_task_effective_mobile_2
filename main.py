from library import Library, DATA_FILE


def main() -> None:
    """
    Основная функция, запускающая интерфейс командной строки для управления библиотекой.
    Позволяет пользователю выбрать одну из доступных операций.
    """
    library = Library(DATA_FILE)

    while True:

        print("\nСистема управления библиотекой")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книг")
        print("4. Список книг")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Введите ваш выбор: ").strip()

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, year)

        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            library.remove_book(book_id)

        elif choice == "3":
            search_type = input("Поиск по (названию/автору/году): ").strip().lower()
            search_query = input("Введите запрос поиска: ").strip()
            results = library.search_books(search_type, search_query)
            if results:
                for book in results:
                    print(
                        f"{book.id}: {book.title} автор: {book.author} ({book.year}) - {book.status}"
                    )
            else:
                print("Не найдено книг, соответствующих запросу.")

        elif choice == "4":
            books = library.list_books()
            if books:
                for book in books:
                    print(
                        f"{book.id}: {book.title} автор: {book.author} ({book.year}) - {book.status}"
                    )
            else:
                print("В библиотеке нет книг.")

        elif choice == "5":
            book_id = int(input("Введите ID книги: "))
            new_status = input("Введите новый статус ('в наличии'/'выдана'): ").strip()
            library.change_status(book_id, new_status)

        elif choice == "6":
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
