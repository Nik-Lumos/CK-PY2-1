if __name__ == "__main__":
    class Game:
        """ Базовый класс компьютерной игры в библиотеке пользователя (по аналогии со Steam) """
        def __init__(self, name: str, total_achievements: int):
            self._name = name
            self._total_achievements = total_achievements
            self._current_achievements = 0  # По умолчанию 0, когда игра попадает в библиотеку пользователя
            self.play_time = 0.01  # По умолчанию 0.01 (потому что float), когда игра попадает в библиотеку пользователя

        # Решено делать защищенными все атрибуты через свойства
        # По логике у обычного пользователя не должно быть прямого доступа ни к одному из них

        @property
        def name(self) -> str:
            """ Возвращает название игры """
            return self._name

        @property
        def total_achievements(self) -> int:
            """ Возвращает общее количество достижений в данной игре """
            return self._total_achievements

        @property
        def current_achievements(self) -> int:
            """ Возвращает количество заработанных достижений """
            return self._current_achievements

        def new_achievement(self) -> None:
            """
            Увеличивает количество заработанных достижений на 1 (при получении достижения).
            Также оповещает пользователя о том, что он получил достижение.
            Если количество достижений уже максимальное, то увеличение не срабатывает и выводится соответствующее сообщение.
            """
            if self.current_achievements == self.total_achievements:
                print("Все достижения уже получены")
            else:
                self._current_achievements += 1
                print("Вы получили новое достижение!")

        def achievement_progress(self) -> None:
            """ Печатает прогресс получения достижений в абсолютных и относительных числах """
            achievement_percent = self.current_achievements * 100 // self.total_achievements  # Считаем процент
            print(f"Достижения: {self.current_achievements}/{self.total_achievements}. Прогресс: {achievement_percent}%")

        @property
        def play_time(self) -> float:
            """ Возвращает количество времени, которое пользователь провел в данной игре """
            return self._play_time

        @play_time.setter
        def play_time(self, new_time: float) -> None:
            """ Устанавливает количество наигранного времени """
            if not isinstance(new_time, float):
                raise TypeError("Количество наигранного времени должно быть типа float")
            if new_time <= 0:
                raise ValueError("Количество наигранного времени должно быть положительным")
            self._play_time = new_time

        def play_time_print(self) -> None:
            """ Печатает количество наигранного времени. Впоследствии будет перегружаться """
            print(f"Вы играли {self.play_time} часов")

        def __str__(self):
            """ Возвращает общее описание экземпляра класса """
            # Данный магический метод будет наследоваться, так как тут выводится общая информация для пользователя
            return f'Игра "{self.name}". Наиграно {self.play_time} часов'

        def __repr__(self):
            """ Возвращает детальное описание экземпляра класса """
            # Данный магический метод будет перегружаться в дочерних классах, чтобы он отображал все атрибуты
            return f'{self.__class__.__name__}(name={self.name!r}, total_achievements={self.total_achievements!r}, current_achievements={self.current_achievements!r}, play_time={self.play_time!r})'

    class SinglePlayerGame(Game):
        """
        Дочерний класс однопользовательской игры.
        Так как в этих играх есть конец, добавим атрибут duration.
        """
        def __init__(self, name: str, total_achievements: int, duration: float):
            super().__init__(name, total_achievements)  # Наследуем атрибуты конструктора базового класса
            self.duration = duration

        @property
        def duration(self) -> float:
            """ Возвращает длительность игры """
            return self._duration

        @duration.setter
        def duration(self, new_duration: float) -> None:
            """ Устанавливает длительность игры """
            if not isinstance(new_duration, float):
                raise TypeError("Длительность игры должна быть типа float")
            if new_duration <= 0:
                raise ValueError("Длительность игры должна быть положительной")
            self._duration = new_duration

        def play_time_print(self) -> None:
            """
            Печатает количество наигранного времени и дополнительно относительный прогресс.
            Поэтому перегружаем его.
            """
            play_time_percent = self.play_time * 100 // self.duration  # Считаем процент от общей продолжительности игры
            # Учтем момент, если игрок будет переигрывать и тем самым проводить больше времени в игре
            if play_time_percent > 100:
                play_time_percent = 100
            print(f"Вы играли {self.play_time} из {self.duration} часов. Прогресс: {play_time_percent}%")

        def __repr__(self):
            """ Возвращает детальное описание экземпляра класса """
            # Перегружаем и добавляем атрибут длительности игры
            return f'{self.__class__.__name__}(name={self.name!r}, total_achievements={self.total_achievements!r}, current_achievements={self.current_achievements!r}, play_time={self.play_time!r}, duration={self.duration!r})'

    class MultiPlayerGame(Game):
        """
        Дочерний класс многопользовательской игры
        (имеются в виду игры, в которых игроки играют друг с другом, а не просто вместе проходят игру).
        В классе не нужен атрибут duration, так как в данные игры можно играть до бесконечности.
        Вместо этого добавим атрибут player_num, который отвечает за количество игроков.
        """
        def __init__(self, name: str, total_achievements: int, player_num: int):
            super().__init__(name, total_achievements)  # Наследуем атрибуты конструктора базового класса
            self.player_num = player_num

        @property
        def player_num(self) -> int:
            """ Возвращает количество игроков, которое необходимо для игры """
            return self._player_num

        @player_num.setter
        def player_num(self, new_player_num: int) -> None:
            """ Устанавливает количество игроков """
            if not isinstance(new_player_num, int):
                raise TypeError("Количество игроков должно быть типа int")
            if new_player_num <= 0:
                raise ValueError("Количество игроков должно быть положительным")
            self._player_num = new_player_num

        def __repr__(self):
            """ Возвращает детальное описание экземпляра класса """
            # Перегружаем и добавляем атрибут количества игроков
            return f'{self.__class__.__name__}(name={self.name!r}, total_achievements={self.total_achievements!r}, current_achievements={self.current_achievements!r}, play_time={self.play_time!r}, player_num={self.player_num!r})'

    # Пусть пользователь приобрел 3 игры
    game_1 = Game("Sims 3", 2)
    game_2 = SinglePlayerGame("NieR: Automata", 47, 60.2)
    game_3 = MultiPlayerGame("Overwatch", 50, 12)

    # Имитируем поведение пользователя
    game_1.new_achievement()  # Вы получили новое достижение!
    game_1.new_achievement()  # Вы получили новое достижение!
    game_1.new_achievement()  # Все достижения уже получены
    game_1.new_achievement()  # Все достижения уже получены
    game_1.play_time = 12.3
    game_1.achievement_progress()  # Достижения: 2/2. Прогресс: 100.0%
    game_1.play_time_print()  # Вы играли 12.3 часов
    print(game_1)  # Игра "Sims 3". Наиграно 12.3 часов
    print(game_1.__repr__())  # Game(name='Sims 3', total_achievements=2, current_achievements=2, play_time=12.3)

    print()

    game_2.new_achievement()  # Вы получили новое достижение!
    game_2.new_achievement()  # Вы получили новое достижение!
    game_2.play_time = 21.1
    game_2.achievement_progress()  # Достижения: 2/47. Прогресс: 4%
    game_2.play_time_print()  # Вы играли 21.1 из 60.2 часов. Прогресс: 35.0%
    print(game_2)  # Игра "NieR: Automata". Наиграно 21.1 часов
    print(game_2.__repr__())  # SinglePlayerGame(name='NieR: Automata', total_achievements=47, current_achievements=2, play_time=21.1, duration=60.2)

    print()

    game_3.new_achievement()  # Вы получили новое достижение!
    game_3.play_time = 105.6
    game_3.achievement_progress()  # Достижения: 1/50. Прогресс: 2%
    game_3.play_time_print()  # Вы играли 105.6 часов
    print(game_3)  # Игра "Overwatch". Наиграно 105.6 часов
    print(game_3.__repr__())  # MultiPlayerGame(name='Overwatch', total_achievements=50, current_achievements=1, play_time=105.6, player_num=12)

    pass
