from typing import Optional, List, Any, Dict


class Product:
    """Класс для представления товаров."""

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

    @classmethod
    def new_product(cls, product_data: Dict[str, Any], products_list: Optional[List["Product"]] = None) -> "Product":
        """Класс-метод для создания объекта Product из словаря с параметрами. Проверяет наличие товара с таким же
        именем в списке products_list."""
        # Извлекаем параметры из словаря
        name: str = product_data.get("name", "")
        description: str = product_data.get("description", "")
        price: float = product_data.get("price", 0.0)
        quantity: int = product_data.get("quantity", 0)

        # Если передан список товаров, ищем дубликаты
        if products_list:
            for existing_product in products_list:
                # Проверяем, есть ли товар с таким же именем
                if existing_product.name == name:
                    # При конфликте цен выбираем более высокую
                    existing_product.price = max(existing_product.price, price)
                    # Суммируем количество
                    existing_product.quantity += quantity
                    # Обновляем описание (можно оставить старое или заменить на новое)
                    # Здесь заменяем на новое описание
                    existing_product.description = description
                    print(
                        f"Товар '{name}' уже существует. Обновлено: "
                        f"цена={existing_product.price}, количество={existing_product.quantity}"
                    )
                    return existing_product

        # Если дубликатов не найдено или список не передан, создаем новый объект
        new_product = cls(name, description, price, quantity)
        return new_product

    @property
    def price(self) -> float:
        """Геттер возвращает текущую цену товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер устанавливает новую цену товара. Проверяет, что цена положительная. При понижении цены
        запрашивает подтверждение у пользователя."""
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

    def __add__(self, other: "Product") -> float:
        """Возвращает полную стоимость всех товаров на складе. Умножает стоимость и количество всех товаров
        в наличии."""
        if type(other) is Product:
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError("Ошибка: нельзя сложить объекты разных классов.")


if __name__ == "__main__":  # pragma: no cover
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    if new_product:
        print(new_product.name)
        print(new_product.description)
        print(new_product.price)
        print(new_product.quantity)

        new_product.price = 800
        print(new_product.price)

        new_product.price = -100
        print(new_product.price)
        new_product.price = 0
        print(new_product.price)

        print(str(product1))
        print(str(product2))
        print(str(product3))

        print(product1 + product2)
        print(product1 + product3)
        print(product2 + product3)
