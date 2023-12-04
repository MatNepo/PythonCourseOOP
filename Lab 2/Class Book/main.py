from typing import Optional
from pydantic import BaseModel

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

    id: int
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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
