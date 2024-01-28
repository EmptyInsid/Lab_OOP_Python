class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажной книги"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __str__(self) -> str:
        return f"Бумажная книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """Класс аудио книги"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = new_duration

    def __str__(self) -> str:
        return f"Аудио книга {self.name}. Автор {self.author}. Продолжительность {self.duration} минут"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


def check_book_info(book: Book) -> None:
    """Вспомогательная функция проверки методов __str__ и __repr__ книг"""
    print(str(book))
    print(repr(book))
    print()


if __name__ == "__main__":
    base_book = Book("Лекартсво от меланхолии", "Рей Брэдбери")
    check_book_info(base_book)

    paper_book = PaperBook("1984", "Джордж Оруэлл", 349)
    check_book_info(paper_book)

    audio_book = AudioBook("Трудно быть богом", "Аркадий и Борис Стругацкие", 306.0)
    check_book_info(audio_book)
