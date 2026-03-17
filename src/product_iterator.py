from src.category import Category
from src.product import Product


class ProductIterator:
    """Итератор для перебора товаров одной категории. Принимает на вход объект класса категории и производит
    итерацию по товарам, которые хранятся в данной категории."""

    category_obj: Category

    def __init__(self, category_object: Category) -> None:
        """Метод для инициализации итератора."""
        self.category = category_object
        self.__products = category_object.product_list
        self.index = 0

    def __iter__(self) -> "ProductIterator":
        """Возвращает итератор."""
        self.index = 0
        return self

    def __next__(self) -> Product:
        """Возвращает следующий очередной товар категории."""
        if self.index < len(self.__products):
            product = self.__products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main__":  # pragma: no cover
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    iterator = ProductIterator(category1)

    for product in iterator:
        print(product)
    print()
    for product in iterator:
        print(product)
