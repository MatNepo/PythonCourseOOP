from typing import Optional
from pydantic import BaseModel
from typing import List

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


class Book(BaseModel):
    """
    Pydantic-модель, представляющая книгу.

    Attributes:
    - id (int): Уникальный идентификатор книги.
    - name (str): Название книги.
    - pages (Optional[int]): Количество страниц в книге (необязательный атрибут).

    Methods:
    - __str__: Возвращает строковое представление объекта для удобного вывода.
    - __repr__: Возвращает представление объекта в виде строки, которое может быть использовано для воссоздания объекта.

    Usage:
    *** book = Book(id=1, name="Пример", pages=300)
    *** print(book)
    Книга "Пример"
    *** print(repr(book))
    Book(id=1, name='Пример', pages=300)
    """

    id_: int
    name: str
    pages: Optional[int] = None

    def __str__(self):
        """
        Возвращает строковое представление объекта для удобного вывода.
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Возвращает представление объекта в виде строки, которое может быть использовано для воссоздания объекта.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    """
    Класс, представляющий библиотеку книг.

    Attributes:
    - books (List[Book]): Список книг в библиотеке.

    Methods:
    - get_next_book_id: Возвращает идентификатор для добавления новой книги в библиотеку.
    - get_index_by_book_id: Возвращает индекс книги в списке.

    Usage:
    *** empty_library = Library()
    *** print(empty_library.get_next_book_id())
    1
    *** list_books = [Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE]
    *** library_with_books = Library(books=list_books)
    *** print(library_with_books.get_next_book_id())
    *** print(library_with_books.get_index_by_book_id(1))
    """

    def __init__(self, books: List[Book] = None):
        self.books = books or []

    def get_next_book_id(self):
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.
        """
        if not self.books:
            return 1
        return max(book.id_ for book in self.books) + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги в списке.
        Если книги с запрашиваемым id не существует, вызывается ошибка ValueError.
        """
        for i, book in enumerate(self.books):
            if book.id_ == book_id:
                return i
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
