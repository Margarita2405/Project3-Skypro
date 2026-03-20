import pytest
from pytest import CaptureFixture

from src.category import Category
from src.exceptions import ZeroQuantityProduct
from src.lawngrass import LawnGrass
from src.order import Order
from src.product import Product
from src.smartphone import Smartphone


def test_order_initialization() -> None:
    """Проверка корректной инициализации заказа."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    order = Order("Заказ №1", "Срочная доставка", product1, 3)

    assert order.name == "Заказ №1"
    assert order.description == "Срочная доставка"
    assert order.product == product1
    assert order.quantity == 3


def test_order_total_cost() -> None:
    """Проверка расчёта итоговой стоимости заказа."""
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    order = Order("Заказ №2", "Обычный", product2, 2)
    assert order.total_cost() == 420000.0


def test_order_string_representation() -> None:
    """Проверка строкового представления заказа."""
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    order = Order("Заказ №3", "Для клиента", product3, 4)
    expected = (
        "Заказ: Заказ №3 | Для клиента\n"
        "Товар: Xiaomi Redmi Note 11, количество: 4, стоимость: 31000.0 руб.\n"
        "Стоимость заказа: 124000.0 руб."
    )
    assert str(order) == expected


def test_order_count_increments() -> None:
    """Проверка увеличения счётчика заказов при создании новых экземпляров."""
    # Сбрасываем счётчик (если необходимо, можно использовать reload, но проще создать тест изолированно)
    Order.order_count = 0
    product = Product("Тест", "Описание", 100.0, 1)

    Order("О1", "", product, 1)
    assert Order.order_count == 1

    Order("О2", "", product, 2)
    assert Order.order_count == 2


def test_order_with_smartphone() -> None:
    """Заказ может содержать объект класса Smartphone (наследник Product)."""
    smartphone = Smartphone(
        name="IPhone 15",
        description="512GB, Gray",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="iPhone 15",
        memory=512,
        color="Gray space",
    )
    order = Order("Смартфон", "Премиум", smartphone, 1)
    assert order.total_cost() == 210000.0
    assert smartphone.name in str(order)


def test_order_with_lawngrass() -> None:
    """Заказ может содержать объект класса LawnGrass (наследник Product)."""
    grass = LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=450.0,
        quantity=15,
        country="США",
        germination_period="5 дней",
        color="Темно-зелёный",
    )
    order = Order("Газонная трава", "Элитная трава для газона", grass, 10)
    assert order.total_cost() == 4500.0
    assert grass.name in str(order)


def test_order_polymorphism_with_category() -> None:
    """Проверка полиморфного использования метода total_cost у Category и Order."""
    # Создаём продукты
    product1 = Product("Товар A", "Описание A", 100.0, 5)
    product2 = Product("Товар B", "Описание B", 200.0, 3)

    # Категория с двумя товарами
    category = Category("Категория", "Описание категории", [product1, product2])

    # Заказ на один товар
    order = Order("Заказ", "Описание заказа", product1, 2)

    # Проверяем разные реализации total_cost
    assert category.total_cost() == (100 * 5 + 200 * 3)  # 500 + 600 = 1100
    assert order.total_cost() == 100 * 2  # 200

    # Оба объекта можно обрабатывать через общий интерфейс
    entities = [category, order]
    costs = [e.total_cost() for e in entities]
    assert costs == [1100.0, 200.0]


def test_order_init_zero_quantity(capsys: CaptureFixture[str]) -> None:
    """
    Проверяет, что при создании заказа с нулевым количеством:
    - выбрасывается исключение ZeroQuantityProduct;
    - сообщение об ошибке выводится;
    - блок finally выводит сообщение о завершении обработки;
    - объект не создаётся (счётчик заказов не увеличивается).
    """
    product = Product("Товар", "Описание", 100.0, 5)
    initial_count = Order.order_count

    with pytest.raises(ZeroQuantityProduct, match="Нельзя добавлять товар с нулевым количеством."):
        Order("Заказ", "Описание", product, 0)

    # Счётчик не должен увеличиться
    assert Order.order_count == initial_count

    captured = capsys.readouterr()
    assert "Нельзя добавлять товар с нулевым количеством." in captured.out
    assert "Обработка добавления товара завершена." in captured.out
    assert "Товар добавлен успешно." not in captured.out


def test_order_init_positive_quantity(capsys: CaptureFixture[str]) -> None:
    """
    Проверяет успешное создание заказа с положительным количеством:
    - объект создаётся;
    - счётчик заказов увеличивается;
    - выводятся сообщения об успехе и завершении обработки.
    """
    product = Product("Товар", "Описание", 100.0, 5)
    initial_count = Order.order_count

    order = Order("Заказ", "Описание", product, 3)

    assert order.name == "Заказ"
    assert order.description == "Описание"
    assert order.product == product
    assert order.quantity == 3
    assert Order.order_count == initial_count + 1

    captured = capsys.readouterr()
    assert "Товар добавлен успешно." in captured.out
    assert "Обработка добавления товара завершена." in captured.out
    assert "Нельзя добавлять товар с нулевым количеством." not in captured.out
