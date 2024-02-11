import doctest
from typing import Union


class MusicInstrument:
    """Класс музыкальных инструментов"""

    def __init__(self, name: str, tune_lvl: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Музыкальный инструмент"
        :param name: название музыкального инструмента (str)
                     полезащищённое так как не предполагается изменение названия после создания
        :param tune_lvl: уровень настройки музвкального инструмента (int, float)
                         поле защищённое, так как требует проверки перед присвоением

        :raise TypeError: Если параметры не соответсвуют требуемым типам, то вызываем ошибку
        :raise ValueError: Если значения параметров не соответсвуют допустимым значениям, то вызываем ошибку

        Примеры:
        >>> music_instrument = MusicInstrument("Хороший инструмент", 10)  # инициализация экземпляра класса
        >>> music_instrument_bad = MusicInstrument("Плохой инструмент", "10")  # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        TypeError: Уровень для настройки должен быть типа int или float
        >>> music_instrument_bad2 = MusicInstrument("Очень плохой инструмент", -10)  # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        ValueError: Уровень для настройки должен быть неотрицательным числом
        """

        self._name = name
        self.tune_lvl = tune_lvl

    @property
    def name(self) -> str:
        """Геттер для названия инструмента"""

        return self._name

    @property
    def tune_lvl(self) -> Union[int, float]:
        """Геттер для уровня настройки инструмента"""

        return self._tune_lvl

    @tune_lvl.setter
    def tune_lvl(self, new_tune_lvl: Union[int, float]) -> None:
        """
        Сеттер уровня настройки инструмента

        :param new_tune_lvl: новый уровень настройки (int, float)

        :raise TypeError: Если параметры не соответсвуют требуемым типам, то вызываем ошибку
        :raise ValueError: Если значения параметров не соответсвуют допустимым значениям, то вызываем ошибку

        Примеры:
        >>> music_instrument = MusicInstrument("Хороший инструмент", 10)  # инициализация экземпляра класса
        >>> music_instrument_bad = MusicInstrument("Плохой инструмент", "10")  # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        TypeError: Уровень для настройки должен быть типа int или float
        >>> music_instrument_bad2 = MusicInstrument("Очень плохой инструмент", -10)  # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        ValueError: Уровень для настройки должен быть неотрицательным числом
        """

        if not isinstance(new_tune_lvl, Union[int, float]):
            raise TypeError("Уровень для настройки должен быть типа int или float")
        if new_tune_lvl < 0:
            raise ValueError("Уровень для настройки должен быть неотрицательным числом")
        self._tune_lvl = new_tune_lvl

    def __str__(self) -> str:
        """Метод для получения общей информации о музыкальном инструмента в виде строки"""

        return f"Инструмент {self.name}. Уровень настройки {self.tune_lvl}"

    def __repr__(self) -> str:
        """Метод для отображения имени и всех значений атрибутов класса"""

        return f"{self.__class__.__name__}(name={self.name!r}, tune_lvl={self.tune_lvl!r})"

    def play(self) -> None:
        """
        Метод для игры на музыкальном инструменте

        Примеры:
        >>> music_instrument = MusicInstrument("Хороший инструмент", 10)
        >>> music_instrument.play()
        Играет Хороший инструмент
        """

        print(f"Играет {self.name}")

    def is_tune(self, new_tune_lvl: Union[int, float]) -> bool:
        """
        Метод для проверки настроен ли музыкальный инструмент

        :param new_tune_lvl: новый уровень настройки (int, float)

        :return: настроен ли инструмент (bool)

        :raise TypeError: Если параметры не соответсвуют требуемым типам, то вызываем ошибку
        :raise ValueError: Если значения параметров не соответсвуют допустимым значениям, то вызываем ошибку

        Примеры:
        >>> music_instrument = MusicInstrument("Хороший инструмент", 10)
        >>> music_instrument.is_tune(50)
        False
        >>> music_instrument.is_tune(10)
        True
        """

        if not isinstance(new_tune_lvl, Union[int, float]):
            raise TypeError("Уровень для настройки должен быть типа int или float")
        if new_tune_lvl < 0:
            raise ValueError("Уровень для настройки должен быть неотрицательным числом числом")
        return self.tune_lvl == new_tune_lvl

    def tune(self, new_tune_lvl: Union[int, float]) -> None:
        """
        Метод для настройки музыкального инструемнта до заданного уровня

        :param new_tune_lvl: новый уровень настройки (int, float)

        :raise TypeError: Если параметры не соответсвуют требуемым типам, то вызываем ошибку
        :raise ValueError: Если значения параметров не соответсвуют допустимым значениям, то вызываем ошибку

        Примеры:
        >>> music_instrument = MusicInstrument("Хороший инструмент", 10)
        >>> music_instrument.tune(10)
        Хороший инструмент уже настроен
        >>> music_instrument.tune(20)
        Настройка Хороший инструмент до уровня 20
        """

        if self.is_tune(new_tune_lvl):
            print(f"{self.name} уже настроен")
        else:
            self.tune_lvl = new_tune_lvl
            print(f"Настройка {self.name} до уровня {self.tune_lvl}")


class Guitar(MusicInstrument):
    """Класс гитары - вид музкального  инструмента"""

    def __init__(self, name: str, tune_lvl: Union[int, float], strings: int):
        """
        Создание и подготовка к работе объекта "Гитара"
        :param name: название музыкального инструмента (str)
                     полезащищённое так как не предполагается изменение названия после создания
        :param tune_lvl: уровень настройки музвкального инструмента (int, float)
                         поле защищённое, так как требует проверки перед присвоением
        :param strings: количество струн у гитары (int)
                        поле приватное так как изменение количсетва струн на гитаре
                        после создания не предполгается

        :raise TypeError: Если параметры не соответсвуют требуемым типам, то вызываем ошибку
        :raise ValueError: Если значения параметров не соответсвуют допустимым значениям, то вызываем ошибку

        Примеры:
        >>> guitar = Guitar("Акустическая гитара", 25, 6)  # инициализация экземпляра класса
        >>> guitar_bad = Guitar("Акустическая гитара", 25, "6")  # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        TypeError: Количество струн у гитары должно быть типа int
        >>> guitar_bad2 = Guitar("Акустическая гитара", 25, -6)  # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        ValueError: Количество струн у гитары должно быть неотрицательным числом
        """
        super().__init__(name, tune_lvl)
        self.strings = strings

    @property
    def strings(self) -> int:
        """Геттер количества струн гитары"""

        return self.__strings

    @strings.setter
    def strings(self, new_strings: int) -> None:
        """
        Сеттер для струн гитары

        :param new_strings: новое количество струн у гитары (int)

        :raise TypeError: Если параметры не соответсвуют требуемым типам, то вызываем ошибку
        :raise ValueError: Если значения параметров не соответсвуют допустимым значениям, то вызываем ошибку

        Примеры:
        >>> guitar = Guitar("Акустическая гитара", 25, 6)  # инициализация экземпляра класса
        >>> guitar.strings("6") # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        TypeError: Количество струн у гитары должно быть типа int
        >>> guitar.strings(-6)
        Traceback (most recent call last):
        ...
        ValueError: Количество струн у гитары должно быть неотрицательным числом
        """

        if not isinstance(new_strings, int):
            raise TypeError("Количество струн у гитары должно быть типа int")
        if new_strings < 0:
            raise ValueError("Количество струн у гитары должно быть неотрицательным числом")

        self.__strings = new_strings

    def __repr__(self) -> str:
        """Перегрузка метода для вывода более подробной информации о классе"""

        return f"{self.__class__.__name__}(name={self.name!r}, tune_lvl={self.tune_lvl!r}), strings={self. strings!r})"

    def play(self) -> None:
        """
        Перегруженный метод игры на гитаре с использованием струн
        Метод перегружен, так как:
            способ игры на гитаре отличается от других инструментов (использование струн);
            гитара издаёт свой звук "Трунь"
            использование уменьшает настроенность гитары на локальную переменную LOOS_OF_TUNING = 0.5

        Примеры:
        >>> guitar = Guitar("Акустическая гитара", 25, 6)
        >>> guitar.play()
        Играет Акустическая гитара
        Играется бой и перебор на 6 струнах. Трунь
        """

        super().play()
        print(f"Играется бой и перебор на {self.strings} струнах. Трунь")
        LOOS_OF_TUNING = 0.5
        if self.tune_lvl >= LOOS_OF_TUNING:
            self.tune_lvl -= LOOS_OF_TUNING

    def play_fingerstyle(self) -> None:
        """
        Метод игры на гитаре в стиле фингерстаил
        Уменьшает настроенность гитары на локальную переменную LOOS_OF_TUNING = 0.8

        Примеры:
        >>> guitar = Guitar("Акустическая гитара", 25, 6)
        >>> guitar.play_fingerstyle()
        Вы дёргаете струны Акустическая гитара и ударяете по гитаре создавая объёмную мелодию. Вы великолепны!
        """

        print(f"Вы дёргаете струны {self.name} и ударяете по гитаре создавая объёмную мелодию. Вы великолепны!")
        LOOS_OF_TUNING = 0.8
        if self.tune_lvl >= LOOS_OF_TUNING:
            self.tune_lvl -= LOOS_OF_TUNING


class Piano(MusicInstrument):
    """Класс пианино - вид музыкального инструмента"""

    def __init__(self, name: str, tune_lvl: Union[int, float], num_keys: int):
        """
        Создание и подготовка к работе объекта "Пианино"
        :param name: название музыкального инструмента (str)
                     полезащищённое так как не предполагается изменение названия после создания
        :param tune_lvl: уровень настройки музвкального инструмента (int, float)
                         поле защищённое, так как требует проверки перед присвоением
        :param num_keys: количество клавиш у пианино (int)
                        поле приватное так как изменение количества клавиш у пианино
                        после создания не предполагается

        :raise TypeError: Если параметры не соответсвуют требуемым типам, то вызываем ошибку
        :raise ValueError: Если значения параметров не соответсвуют допустимым значениям, то вызываем ошибку

        Примеры:
        >>> piano = Piano("Большое пианино", 20, 88)  # инициализация экземпляра класса
        >>> piano_bad = Piano("Большое пианино", 20, "88")  # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        TypeError: Количество клавиш у пианино должно быть типа int
        >>> piano_bad2 = Piano("Большое пианино", 25, -88)  # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        ValueError: Количество клавиш у пианино должно быть неотрицательным числом
        """

        super().__init__(name, tune_lvl)
        self.num_keys = num_keys

    @property
    def num_keys(self) -> int:
        """Геттер для количества клавиш пианино"""

        return self.__num_keys

    @num_keys.setter
    def num_keys(self, new_num_keys: int) -> None:
        """
        Сеттер для клавиш пианино

        :param new_num_keys: количество клавиш у пианино (int)
                        поле приватное так как изменение количества клавиш у пианино
                        после создания не предполагается

        :raise TypeError: Если параметры не соответсвуют требуемым типам, то вызываем ошибку
        :raise ValueError: Если значения параметров не соответсвуют допустимым значениям, то вызываем ошибку

        Примеры:
        >>> piano = Piano("Большое пианино", 20, 88)  # инициализация экземпляра класса
        >>> piano.num_keys("88")
        Traceback (most recent call last):
        ...
        TypeError: Количество клавиш у пианино должно быть типа int
        >>> piano.num_keys(-88)
        Traceback (most recent call last):
        ...
        ValueError: Количество клавиш у пианино должно быть неотрицательным числом
        """

        if not isinstance(new_num_keys, int):
            raise TypeError("Количество клавиш у пианино должно быть типа int")
        if new_num_keys < 0:
            raise ValueError("Количество клавиш у пианино должно быть неотрицательным числом")

        self.__num_keys = new_num_keys

    def __repr__(self) -> str:
        """Перегрузка метода для вывода более подробной информации о классе"""

        return f"{self.__class__.__name__}(name={self.name!r}, tune_lvl={self.tune_lvl!r}, num_keys={self.num_keys!r})"

    def play(self) -> None:
        """
        Перегруженный метод игры на пианино с использованием клавиш
        Метод перегружен, так как:
            способ игры на пианино отличается от других инструментов (использование клавиш);
            пианино издаёт свой звук "Пам-пам-пам"
            использование уменьшает настроенность пианино на локальную переменную LOOS_OF_TUNING = 0.7

        Примеры:
        >>> piano = Piano("Большое пианино", 20, 88)
        >>> piano.play()
        Играет Большое пианино
        Используются все 88 клавиш. Пам-пам-пам
        """

        super().play()
        print(f"Используются все {self.num_keys} клавиш. Пам-пам-пам")
        LOOS_OF_TUNING = 0.7
        if self.tune_lvl >= LOOS_OF_TUNING:
            self.tune_lvl -= LOOS_OF_TUNING

    def press_pedal(self) -> None:
        """
        Метод нажатие педли пианино

        Примеры:
        >>> piano = Piano("Большое пианино", 20, 88)
        >>> piano.press_pedal()
        Нажимается педаль у Большое пианино пианино
        """

        print(f"Нажимается педаль у {self.name} пианино")


def check_music_instrument(music_instrument: MusicInstrument) -> None:
    tune_lvl = 70
    print(music_instrument.__str__())
    print(music_instrument.__repr__())
    music_instrument.tune(tune_lvl)
    music_instrument.play()


if __name__ == "__main__":
    doctest.testmod()

    base_music_instrument = MusicInstrument("Базовый инструмент", 50)
    check_music_instrument(base_music_instrument)
    print()

    electro_guitar = Guitar("Электро гитара", 100, 8)
    check_music_instrument(electro_guitar)
    electro_guitar.play_fingerstyle()
    print()

    mini_piano = Piano("Мини-пианино", 80, 61)
    check_music_instrument(mini_piano)
    mini_piano.press_pedal()
    print()


