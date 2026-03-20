from src.base_entity import BaseEntity
from src.category import Category
from src.exceptions import ZeroQuantityProduct
from src.product import Product


class Order(BaseEntity):
    """Класс для представления заказа (один товар)."""

    # Счётчик заказов
    order_count = 0

    def __init__(self, name: str, description: str, product: Product, quantity: int) -> None:
        """
        :param name: название заказа (например, "Заказ №1")
        :param description: описание заказа
        :param product: товар (объект класса Product или его наследника)
        :param quantity: количество единиц товара
        """
        super().__init__(name, description)
        try:
            if quantity == 0:
                raise ZeroQuantityProduct("Нельзя добавлять товар с нулевым количеством.")
            self.product = product
            self.quantity = quantity
            Order.order_count += 1
            print("Товар добавлен успешно.")
        except ZeroQuantityProduct as e:
            print(str(e))
            raise
        finally:
            print("Обработка добавления товара завершена.")

    def total_cost(self) -> float:
        """Итоговая стоимость заказа."""
        return self.product.price * self.quantity

    def __str__(self) -> str:
        """Возвращает строку с информацией о заказе."""
        return (
            f"Заказ: {self.name} | {self.description}\n"
            f"Товар: {self.product.name}, количество: {self.quantity}, "
            f"стоимость: {self.product.price} руб.\n"
            f"Стоимость заказа: {self.total_cost()} руб."
        )


if __name__ == "__main__":  # pragma: no cover
    # Создаем товары
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем категорию
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    print(category1)
    print(f"Общая стоимость товаров в категории: {category1.total_cost()} руб.")

    # Создаем заказ
    order = Order("Заказ №1", "Срочная доставка", product1, 2)
    print(order)

    print("Пытаемся создать заказ с нулевым количеством:")
    try:
        order = Order("Заказ №1", "Тестовый заказ", product1, 0)
    except ZeroQuantityProduct as e:
        print(f"Исключение перехвачено: {e}")

    print(f"\nОбщее количество заказов (счётчик): {Order.order_count}")
