if __name__ == "__main__":
    # Write your solution here
    class Phone:
        """Базовый класс телефона"""

        def __init__(self, brand: str, model: str, storage: int):
            """Инициализация телефона"""
            self.brand: str = brand
            self.model: str = model
            self.storage: int = storage

            # Скрытый атрибут: IMEI не должен изменяться напрямую
            self.__imei: str = "000000000000000"

        def get_info(self) -> str:
            """Возвращает информацию о телефоне"""
            return f"{self.brand} {self.model}, {self.storage}GB"

        def call(self, number: str) -> None:
            """Совершить звонок."""
            print(f"Calling {number} from {self.brand} {self.model}")

        def __str__(self) -> str:
            return f"Phone: {self.brand} {self.model}"

        def __repr__(self) -> str:
            return f"Phone(brand='{self.brand}', model='{self.model}', storage={self.storage})"


    class SmartPhone(Phone):
        """Дочерний класс смартфона"""

        def __init__(self, brand: str, model: str, storage: int, os: str):
            """Расширенный конструктор"""
            super().__init__(brand, model, storage)
            self.os: str = os

        def get_info(self) -> str:
            """
            Перегрузка метода get_info.

            Причина: у смартфона важно показывать операционную систему
            """
            base = super().get_info()
            return f"{base}, OS: {self.os}"

        def install_app(self, name: str) -> None:
            """Установить приложение."""
            print(f"Installing {name}")

        def __str__(self) -> str:
            return f"SmartPhone: {self.brand} {self.model}"

        def __repr__(self) -> str:
            return f"SmartPhone(brand='{self.brand}', model='{self.model}', storage={self.storage}, os='{self.os}')"


    if __name__ == "__main__":
        phone = SmartPhone("Samsung", "S23", 256, "Android")

        print(phone.get_info())
        phone.call("+723456789")
        phone.install_app("Telegram")

        print(phone)
        print(repr(phone))
    pass
