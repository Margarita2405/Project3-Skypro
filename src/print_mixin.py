class PrintMixin:
    """Класс-миксин для распечатывания в консоль информации об объекте с указанием его класса и параметров."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        """Метод для отображения информации об объекте класса."""
        return f"{self.__class__.__name__}({self.name!r}, {self.description!r}, {self.price}, {self.quantity})"
