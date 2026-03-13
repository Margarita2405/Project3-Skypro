from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Sequence


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер возвращает текущую цену товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер устанавливает новую цену товара. Проверяет, что цена положительная.
        При понижении цены запрашивает подтверждение у пользователя."""
        # Проверка на нулевую или отрицательную цену
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Если цена понижается, запрашиваем подтверждение у пользователя
        if new_price < self.__price:
            print(f"Внимание! Цена понижается с {self.__price} до {new_price}.")
            response = input(
                "Вы уверены, что хотите понизить цену? Если согласны, введите (y), для отмены " "введите (n): "
            )

            if response.lower() != "y":
                print("Изменение цены отменено пользователем.")
                return
        # Установка новой цены
        self.__price = new_price
        print(f"Установлена цена продукта: {self.__price} руб.")

    def __str__(self) -> str:
        """Возвращает строку в формате: Название продукта, цена руб. Остаток: количество шт."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Абстрактный метод сложения товара — каждый наследник реализует свою логику."""
        pass

    @classmethod
    @abstractmethod
    def new_product(
        cls, product_data: Dict[str, Any], products_list: Optional[Sequence["BaseProduct"]] = None
    ) -> "BaseProduct":
        """Абстрактный метод для корректного создания объектов с учётом дополнительных полей — должен быть
        переопределён в наследниках."""
        pass
