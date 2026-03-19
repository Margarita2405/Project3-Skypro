from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Sequence


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов (только интерфейс)."""

    name: str
    description: str
    quantity: int


    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактное свойство - текущая цена товара."""
        pass


    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Абстрактный метод сложения товара — каждый наследник реализует свою логику."""
        pass

    @classmethod
    @abstractmethod
    def new_product(
        cls, product_data: Dict[str, Any], products_list: Optional[Sequence["BaseProduct"]] = None
    ) -> "BaseProduct":
        """Абстрактный метод для корректного создания товара с учётом дополнительных полей — должен быть
        переопределён в наследниках."""
        pass
