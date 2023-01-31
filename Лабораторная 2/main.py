BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books=[]):
        if not isinstance(books, list):
            raise TypeError("Список книг должен быть типа list")
        self.books = books
        self.book_id = 0  # Атрибут для метода get_index_by_book_id

    def get_next_book_id(self) -> int:
        if len(self.books) == 0:  # Если нет книг
            return 1
        else:  # Если книги есть
            last_book = self.books[-1]
            return last_book.id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        self.book_id = book_id
        for i, description in enumerate(self.books):
            if self.book_id == description.id:  # Проверяем, есть ли книга с таким же id
                return i  # Возвращаем индекс списка
            else:
                raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
