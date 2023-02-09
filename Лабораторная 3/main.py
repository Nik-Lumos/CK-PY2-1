class Book:
    """ Базовый класс книги """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Название книги"""
        return self._name

    @property
    def author(self) -> str:
        """Автор книги"""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Подкласс бумажной книги """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Количество страниц в книге"""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Установка количества страниц в книге"""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = new_pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. {self.pages} страниц"


class AudioBook(Book):
    """ Подкласс аудиокниги """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Длительность аудиокниги"""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Установка длительности аудиокниги"""
        if not isinstance(new_duration, float):
            raise TypeError("Длительность аудиокниги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Длительность аудиокниги должна быть положительным")
        self._duration = new_duration

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. {self.duration} часов"
