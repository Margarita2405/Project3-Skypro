from abc import ABC, abstractmethod


class BaseEntity(ABC):
    """Абстрактный базовый класс для сущностей, имеющих название и описание."""

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @abstractmethod
    def total_cost(self) -> float:
        """Абстрактный метод для вычисления общей стоимости. Должен быть переопределён в наследниках."""
        pass
