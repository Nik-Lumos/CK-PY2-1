import doctest


class Column:
    def __init__(self, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Колонна" (квадратная)

        :param width: Ширина колонны в м
        :param height: Высота колонны в м
         Примеры:
        >>> column = Column(0.5, 3)
        """
        if not isinstance(width, (float, int)):
            raise TypeError("Ширина колонны должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина колонны должна быть положительным числом")
        self.width = width

        if not isinstance(height, (float, int)):
            raise TypeError("Высота колонны должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота колонны должна быть положительным числом")
        self.height = height

    def area(self) -> float:
        """
        Функция подсчета площади сечения колонны

        Примеры:
        >>> column = Column(0.5, 3)
        >>> column.area()
        """
        ...

    def volume(self) -> float:
        """
        Функция подсчета объема колонны

        Примеры:
        >>> column = Column(0.5, 3)
        >>> column.volume()
        """
        ...


class Beam:
    def __init__(self, volume: float, load_capacity: float):
        """
        Создание и подготовка к работе объекта "Балка" (железобетонная)

        :param volume: Объем балки
        :param load_capacity: Несущая способность балки
        Примеры:
        >>> beam = Beam(1.92, 11.5)
        """
        if not isinstance(volume, (float, int)):
            raise TypeError("Объем балки должен быть типа int или float")
        if volume <= 0:
            raise ValueError("Объем балки должен быть положительным числом")
        self.volume = volume

        if not isinstance(load_capacity, (float, int)):
            raise TypeError("Несущая способность балки должна быть типа int или float")
        if load_capacity <= 0:
            raise ValueError("Несущая способность балки должна быть положительным числом")
        self.load_capacity = load_capacity

    def weight(self) -> float:
        """
        Функция подсчета веса железобетонной балки

        Примеры:
        >>> beam = Beam(1.92, 11.5)
        >>> beam.weight()
        """
        ...

    def bearing_load(self, load: float) -> bool:
        """
        Функция проверяет, выдерживает ли балка нагрузку

        :param load: Нагрузка, действующая на балку

        Примеры:
        >>> beam = Beam(1.92, 11.5)
        >>> beam.bearing_load(8.9)
        """
        if not isinstance(load, (int, float)):
            raise TypeError("Значение нагрузки должно быть типа int или float")
        if load < 0:
            raise ValueError("Значение нагрузки должно быть положительным числом")
        ...


class Videogame:
    def __init__(self, levels: int, genre: str):
        """
        Создание и подготовка к работе объекта "Видеоигра"

        :param levels: Количество уровней в игре
        :param length: Продолжительность игры в часах
        :param genre: Жанр игры
        Примеры:
        >>> videogame = Videogame(10, "action")
        """
        if not isinstance(levels, int):
            raise TypeError("Количество уровней должно быть целым числом")
        if levels <= 0:
            raise ValueError("Количество уровней должно быть положительным числом")
        self.levels = levels

        if not isinstance(genre, str):
            raise TypeError("Жанр игры должен быть типа str")
        self.genre = genre

    def favourite_genre(self, favourite_genre_list) -> bool:
        """
        Проверка, нравится ли нам жанр игры

        :param favourite_genre_list: Список любимых жанров

        Примеры:
        >>> videogame = Videogame(10, "action")
        >>> videogame.favourite_genre(["rpg", "action", "strategy"])
        """
        if not isinstance(favourite_genre_list, list):
            raise TypeError("Список любимых жанров должен быть типа list")
        ...

    def progress(self, passed_levels: int) -> float:
        """
        Определение прогресса игры

        :param passed_levels: Количество пройденных уровней

        Примеры:
        >>> videogame = Videogame(10, "action")
        >>> videogame.progress(3)
        """
        if not isinstance(passed_levels, int):
            raise TypeError("Количество пройденных уровней должно быть целым числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
