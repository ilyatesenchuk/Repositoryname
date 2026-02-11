# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Window:
    """
    Класс, описывающий окно.

    Атрибуты:
        width (float): Ширина окна в метрах
        height (float): Высота окна в метрах
        is_open (bool): Открыто ли окно
    """

    def __init__(self, width: float, height: float):
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть числом")
        if width <= 0:
            raise ValueError("Ширина должна быть положительной")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть числом")
        if height <= 0:
            raise ValueError("Высота должна быть положительной")
        self.height = height

        self.is_open = False

    def open(self) -> None:
        """Открыть окно."""
        if self.is_open:
            raise ValueError("Окно уже открыто")
        ...

    def close(self) -> None:
        """Закрыть окно."""
        if not self.is_open:
            raise ValueError("Окно уже закрыто")
        ...


class Flashlight:
    """
    Класс, описывающий фонарик.

    Атрибуты:
        battery_level (int): Уровень заряда батареи (0-100)
        is_on (bool): Включен ли фонарик
        brightness (int): Яркость (1-3)
    """

    def __init__(self, battery_level: int):
        if not isinstance(battery_level, int):
            raise TypeError("Уровень заряда должен быть целым числом")
        if battery_level < 0 or battery_level > 100:
            raise ValueError("Уровень заряда должен быть от 0 до 100")
        self.battery_level = battery_level
        self.is_on = False
        self.brightness = 1

    def turn_on(self) -> None:
        """Включить фонарик."""
        if self.battery_level <= 0:
            raise ValueError("Батарея разряжена")
        ...

    def change_brightness(self) -> None:
        """Переключить яркость."""
        ...


class Notebook:
    """
    Класс, описывающий записную книжку.

    Атрибуты:
        pages (int): Количество страниц
        current_page (int): Текущая страница
        cover_color (str): Цвет обложки
    """

    def __init__(self, pages: int, cover_color: str):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.pages = pages

        if not isinstance(cover_color, str):
            raise TypeError("Цвет обложки должен быть строкой")
        if not cover_color.strip():
            raise ValueError("Цвет обложки не может быть пустым")
        self.cover_color = cover_color

        self.current_page = 1

    def turn_page(self) -> None:
        """Перевернуть страницу."""
        if self.current_page >= self.pages:
            raise ValueError("Достигнут конец книжки")
        ...

    def write_note(self, text: str) -> None:
        """
        Записать заметку.

        :param text: Текст заметки
        """
        if not isinstance(text, str):
            raise TypeError("Текст должен быть строкой")
        if not text.strip():
            raise ValueError("Текст не может быть пустым")
        ...


# TODO работоспособность экземпляров класса проверить с помощью doctest

if __name__ == "__main__":
    doctest.testmod()
    pass
