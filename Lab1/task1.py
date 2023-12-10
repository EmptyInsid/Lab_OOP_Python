import doctest
from typing import Union


class Wand:
    def __init__(self, strength: Union[int, float], magic: Union[int, float], material: str):
        """
        Создание и подготовка к работе объекта "Палочка"
        :param strength: Уровень прочности палочки (int, float)
        :param magic: Уровень магии палочки (int, float)
        :param material: Материал палочки (str)

        :raise TypeError: Если параметры не соответсвуют требуемым типам, то вызываем ошибку
        :raise ValueError: Если значения параметров не соответсвуют допустимым значениям, то вызываем ошибку

        Примеры:
        >>> wand = Wand(100, 100, "yew")  # инициализация экземпляра класса
        >>> wand2 = Wand("100", 100, "yew")  # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        TypeError: Прочность палочки должна быть типа int или float
        >>> wand3 = Wand(100, -100, "yew")  # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        ValueError: Магия палочки должна быть положительным числом
        """

        if not isinstance(strength, (int, float)):
            raise TypeError("Прочность палочки должна быть типа int или float")
        if strength <= 0:
            raise ValueError("Прочность палочки должна быть больше нуля")
        self.strength = strength

        if not isinstance(magic, (int, float)):
            raise TypeError("Магия палочки должна быть типа int или float")
        if magic < 0:
            raise ValueError("Магия палочки должна быть положительным числом")
        self.magic = magic

        if not isinstance(material, str):
            raise TypeError("Материал палочки должен быть типа str")
        if material == "":
            raise ValueError("Материал палочки не может быть пустым значением")
        self.material = material

    def can_spell(self) -> bool:
        """
        Функция, которая проверяет является ли палочка волшебной
        :return: Является ли палочка волшебной (bool)

        Примеры:
        >>> wand = Wand(100, 100, "yew")
        >>> wand.can_spell()
        True
        >>> wand = Wand(100, 0, "yew")
        >>> wand.can_spell()
        False
        """

        return self.magic > 0

    def fix(self, add_strength: Union[int, float]) -> None:
        """
        Функция для увеличение прочности палочки (починка)
        :param add_strength: Количество добавляемой прочности (int, float)

        :raise TypeError: Если количество добавляемой прочности не соответсвует типу int или float, то вызываем ошибку
        :raise ValueError: Если количество добавляемой прочности отрицательное число, то вызываем ошибку

        Примеры:
        >>> wand = Wand(100, 100, "yew")
        >>> wand.fix(50)
        >>> wand.fix("50") # ошибочное использование функции
        Traceback (most recent call last):
        ...
        TypeError: Добавочная прочность палочки должна быть типа int или float
        >>> wand.fix(-7) # ошибочное использование функции
        Traceback (most recent call last):
        ...
        ValueError: Добавочная прочность палочки должна быть больше нуля
        """

        if not isinstance(add_strength, (int, float)):
            raise TypeError("Добавочная прочность палочки должна быть типа int или float")
        if add_strength <= 0:
            raise ValueError("Добавочная прочность палочки должна быть больше нуля")
        self.strength += add_strength

    def crack(self, take_strength: Union[int, float]) -> None:
        """
        Функция для меньшения прочности палочки (поломка)
        :param take_strength: Количество отнимаемой прочности (int, float)

        :raise TypeError: Если количество отнимаемой прочности не соответсвует типу int или float, то вызываем ошибку
        :raise ValueError: Если количество отнимаемой прочности отрицательное, то вызываем ошибку

        Примеры:
        >>> wand = Wand(100, 100, "yew")
        >>> wand.crack(50)
        >>> wand.crack("50") # ошибочное использование функции
        Traceback (most recent call last):
        ...
        TypeError: Отнимаемая прочность палочки должна быть типа int или float
        >>> wand.crack(-7) # ошибочное использование функции
        Traceback (most recent call last):
        ...
        ValueError: Отнимаемая прочность палочки должна быть больше нуля
        >>> wand.crack(1000) # ошибочное использование функции
        Traceback (most recent call last):
        ...
        ValueError: Отнимаемая прочность палочки должна быть меньше или равна нынешней прочности палочки
        """

        if not isinstance(take_strength, (int, float)):
            raise TypeError("Отнимаемая прочность палочки должна быть типа int или float")
        if take_strength <= 0:
            raise ValueError("Отнимаемая прочность палочки должна быть больше нуля")
        if take_strength > self.strength:
            raise ValueError("Отнимаемая прочность палочки должна быть меньше или равна нынешней прочности палочки")
        self.strength -= take_strength


class Witch:
    def __init__(self, health: Union[int, float], magic: Union[int, float], wand: Wand):
        """
        Создание и подготовка к работе объекта "Ведьма"
        :param health: Уровень здоровья ведьмы (int, float)
        :param magic: Уровень магии ведьмы (int, float)
        :param wand: Волшебная палочка ведьмы (Wand)

        :raise TypeError: Если параметры не соответсвуют требуемым типам, то вызываем ошибку
        :raise ValueError: Если значения параметров не соответсвуют допустимым значениям, то вызываем ошибку

        Примеры:
        >>> wand_yew = Wand(100, 100, "yew")
        >>> witch = Witch(100, 100, wand_yew)  # инициализация экземпляра класса
        >>> witch1 = Witch(-100, 100, wand_yew) # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        ValueError: Здоровье ведьмы должна быть больше нуля
        >>> witch2 = Witch(100, "100", wand_yew) # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        TypeError: Магия ведьмы должна быть типа int или float
        >>> wand_usual = Wand(100, 0, "tree")
        >>> witch = Witch(100, 100, wand_usual) # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        ValueError: Палочка ведьмы должна быть способна колдовать
        """

        if not isinstance(health, (int, float)):
            raise TypeError("Здоровье ведьмы должна быть типа int или float")
        if health <= 0:
            raise ValueError("Здоровье ведьмы должна быть больше нуля")
        self.health = health

        if not isinstance(magic, (int, float)):
            raise TypeError("Магия ведьмы должна быть типа int или float")
        if magic < 0:
            raise ValueError("Магия ведьмы должна быть положительным числом")
        self.magic = magic

        if not isinstance(wand, Wand):
            raise TypeError("Новая палочка должна принадлежать классу Wand")
        if not wand.can_spell():
            raise ValueError("Палочка ведьмы должна быть способна колдовать")
        self.wand = wand

    def change_wand(self, new_wand: Wand) -> None:
        """
        Функция для изменение палочки ведьмы
        :param new_wand: Новая палочка ведьмы (Wand)

        :raise TypeError: Если новая палочка не относится к классу Wand, то вызываем ошибку
        :raise ValueError: Если новая палочка не может колдовать, то вызываем ошибку

        Примеры:
        >>> wand_yew = Wand(100, 100, "yew")
        >>> witch = Witch(100, 100, wand_yew)
        >>> wand_birch = Wand(100, 100, "birch")
        >>> witch.change_wand(wand_birch)
        >>> wand_bad = Wand(100, 0, "tree")
        >>> witch.change_wand(wand_bad) # ошибочное использование функции
        Traceback (most recent call last):
        ...
        ValueError: Палочка ведьмы должна быть способна колдовать
        >>> witch.change_wand("wand") # ошибочное использование функции
        Traceback (most recent call last):
        ...
        TypeError: Новая палочка должна принадлежать классу Wand
        """

        if not isinstance(new_wand, Wand):
            raise TypeError("Новая палочка должна принадлежать классу Wand")
        if not new_wand.can_spell():
            raise ValueError("Палочка ведьмы должна быть способна колдовать")
        self.wand = new_wand

    def treatment(self, add_health: Union[int, float]) -> None:
        """
        Функция для увеличение здоровья ведьмы (лечение)
        :param add_health: Количество добавляемого здоровья (int, float)

        :raise TypeError: Если количество добавляемого здоровья не соответсвует типу int или float, то вызываем ошибку
        :raise ValueError: Если количество добавляемого здоровья отрицательное число, то вызываем ошибку

        Примеры:
        >>> wand_yew = Wand(100, 100, "yew")
        >>> witch = Witch(100, 100, wand_yew)
        >>> witch.treatment(10)
        >>> witch.treatment("-10") # ошибочное использование функции
        Traceback (most recent call last):
        ...
        TypeError: Добавляемое здоровье должно быть типа int или float
        >>> witch.treatment(-10) # ошибочное использование функции
        Traceback (most recent call last):
        ...
        ValueError: Добавляемое здоровье должно должна быть больше нуля
        """

        if not isinstance(add_health, (int, float)):
            raise TypeError("Добавляемое здоровье должно быть типа int или float")
        if add_health <= 0:
            raise ValueError("Добавляемое здоровье должно должна быть больше нуля")
        self.health += add_health

    def splash_of_magic(self) -> Union[int, float]:
        """
        Функция для всплеска магии ведьмы в бою
        :return: магия ведьмы в квадрате (int, float)

        Примеры:
        >>> wand_yew = Wand(100, 100, "yew")
        >>> witch = Witch(100, 100, wand_yew)
        >>> witch.splash_of_magic()
        10000
        """
        return self.magic*self.magic


class Mantle:
    def __init__(self, length: Union[int, float], price: Union[int, float], material: str):
        """
        Создание и подготовка к работе объекта "Мантия"
        :param length: Длина мантии (int, float)
        :param price: Цена мантии (int, float)
        :param material: Материал мантии (str)

        Примеры:
        >>> mantle = Mantle(150, 300, "silk")  # инициализация экземпляра класса
        >>> mantle1 = Mantle(-150, 300, "silk") # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        ValueError: Длина мантии должна быть больше нуля
        >>> mantle1 = Mantle(150, "300", "silk") # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        TypeError: Цена мантии должна быть типа int или float
        >>> mantle1 = Mantle(150, 300, "") # ошибочная инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        ValueError: Материал мантии не может быть пустым значением
        """

        if not isinstance(length, (int, float)):
            raise TypeError("Длина мантии должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина мантии должна быть больше нуля")
        self.length = length

        if not isinstance(price, (int, float)):
            raise TypeError("Цена мантии должна быть типа int или float")
        if price < 0:
            raise ValueError("Цена мантии должна быть положительным числом")
        self.price = price

        if not isinstance(material, str):
            raise TypeError("Материал мантии должен быть типа str")
        if material == "":
            raise ValueError("Материал мантии не может быть пустым значением")
        self.material = material

    def buy(self, money: Union[int, float]) -> bool:
        """
        Функция для покупки мантии
        :param money: Количество предлагаемых для покупки денег (int, float)

        :return: Бфла ли продана мантия (bool)

        :raise TypeError: Если деньги не соответсвуют типу int или float, то вызываем ошибку
        :raise ValueError: Если количество денег отрицательное число, то вызываем ошибку

        Примеры:
        >>> mantle = Mantle(150, 300, "silk")
        >>> mantle.buy(50)
        False
        >>> mantle.buy(300)
        True
        """

        return self.price <= money

    def sell(self) -> float:
        """
        Функция для продажи мантии и получении денег c вычетом процента от носки
        :return: Количество полученных от продажи денег c вычетом процента от носки (float)

        Примеры:
        >>> mantle = Mantle(150, 300, "silk")
        >>> mantle.sell()
        200.0
        """
        DECREASE = 3  # пример значения для уменьшения цены во время продажи
        percent = self.price / DECREASE
        return self.price - percent


if __name__ == "__main__":
    doctest.testmod()
    pass
