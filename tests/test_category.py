from typing import Any, List

import pytest

from src.category import Category
from src.product import Product


def test_category_init(first_category: Category, second_category: Category) -> None:
    """Тест, который проверяет корректность инициализации объектов класса Category."""
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации, но и получения" " дополнительных функций для удобства жизни"
    )
    assert len(first_category._Category__products) == 3

    assert second_category.name == "Телевизоры"
    assert second_category.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, станет" " вашим другом и помощником"
    )
    assert len(second_category._Category__products) == 1

    # Проверяем подсчет количества категорий
    assert first_category.category_count == 2
    assert second_category.category_count == 2

    # Проверяем подсчет количества товаров
    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_category_attributes(sample_category: Category) -> None:
    """Тест наличия всех необходимых атрибутов класса Category."""
    # Проверяем name
    try:
        name = sample_category.name
        assert name is not None  # Атрибут существует
    except AttributeError:
        assert False, "Атрибут 'name' отсутствует"

    # Проверяем description
    try:
        description = sample_category.description
        assert description is not None  # Атрибут существует
    except AttributeError:
        assert False, "Атрибут 'description' отсутствует"

    # Проверяем products
    try:
        products = sample_category.products
        assert isinstance(products, str)
        assert products != ""  # Проверяем, что строка не пустая
    except AttributeError:
        assert False, "Атрибут 'products' отсутствует"


def test_products_in_category(sample_category: Category) -> None:
    """Тест, что товары в категории являются объектами класса Product."""
    for product in sample_category._Category__products:
        assert isinstance(product, Product)


@pytest.mark.parametrize(
    "invalid_object",
    [
        "строка",
        123,
        45.6,
        None,
        [],
        {},
        object(),
        (1, 2),
        set(),
    ],
)
def test_add_product_invalid_type_raises_typeerror(category: Category, invalid_object: Any) -> None:
    """Тест проверяет, что при попытке добавить объект, не являющийся экземпляром Product
    или его наследника, метод add_product выбрасывает TypeError с ожидаемым сообщением,
    и при этом состояние категории и общий счётчик продуктов не изменяются."""
    # Сохраняем исходное состояние
    initial_products = category._Category__products[:]  # копируем приватный список
    initial_count = Category.product_count

    # Проверяем, что возникает исключение с правильным текстом
    with pytest.raises(
        TypeError, match="Ошибка: нельзя добавлять вместо продукта или его наследников" " любой другой объект."
    ):
        category.add_product(invalid_object)

    # Убеждаемся, что состояние не изменилось
    assert category._Category__products == initial_products
    assert Category.product_count == initial_count


def test_category_counters_after_creating_categories() -> None:
    """Тест счетчиков после создания нескольких категорий."""
    # Сбрасываем счетчики для чистоты теста
    Category.category_count = 0
    Category.product_count = 0

    # Создаем первую категорию с 2 товарами
    product1 = Product("Товар 1", "Описание", 100.0, 1)
    product2 = Product("Товар 2", "Описание", 200.0, 2)
    category1 = Category("Категория 1", "Описание", [product1, product2])

    # Проверяем счетчики и свойства объекта
    assert Category.category_count == 1
    assert Category.product_count == 2
    assert category1.name == "Категория 1"
    assert len(category1._Category__products) == 2

    # Создаем вторую категорию с 3 товарами
    product3 = Product("Товар 3", "Описание", 300.0, 3)
    product4 = Product("Товар 4", "Описание", 400.0, 4)
    product5 = Product("Товар 5", "Описание", 500.0, 5)
    category2 = Category("Категория 2", "Описание", [product3, product4, product5])

    assert Category.category_count == 2
    assert Category.product_count == 5  # 2 + 3
    assert category2.name == "Категория 2"
    assert len(category2._Category__products) == 3

    # Создаем третью категорию без товаров
    category3 = Category("Категория 3", "Описание", [])

    assert Category.category_count == 3
    assert Category.product_count == 5  # не изменилось
    assert category3.name == "Категория 3"

    # Создаем четвертую категорию с None вместо товаров
    category4 = Category("Категория 4", "Описание", [])

    assert Category.category_count == 4
    assert Category.product_count == 5  # не изменилось
    assert category4.name == "Категория 4"


def test_category_counters_with_same_product_in_multiple_categories() -> None:
    """Тест счетчиков, когда один товар в нескольких категориях."""
    Category.category_count = 0
    Category.product_count = 0

    product = Product("Товар", "Описание", 100.0, 1)

    # Один и тот же товар в двух категориях
    category1 = Category("Категория 1", "Описание", [product])
    assert Category.product_count == 1
    assert Category.category_count == 1
    assert product in category1._Category__products
    assert category1.name == "Категория 1"

    category2 = Category("Категория 2", "Описание", [product])
    assert Category.product_count == 2  # Счетчик увеличился, хотя объект один
    assert Category.category_count == 2
    assert product in category2._Category__products
    assert category2.name == "Категория 2"


def test_category_counters_reset() -> None:
    """Тест сброса счетчиков."""
    # Устанавливаем начальные значения
    Category.category_count = 10
    Category.product_count = 20

    # Проверяем, что они установились
    assert Category.category_count == 10
    assert Category.product_count == 20

    # Создаем новую категорию
    product = Product("Товар", "Описание", 100.0, 1)
    category = Category("Категория", "Описание", [product])

    # Проверяем, что счетчики увеличились
    assert Category.category_count == 11
    assert Category.product_count == 21
    assert category.name == "Категория"


def test_product_modification_reflected_in_category() -> None:
    """Тест, что изменение товара отражается в категории."""
    # Создаем товар
    product = Product("Исходное имя", "Исходное описание", 100.0, 5)

    # Создаем категорию с этим товаром
    category = Category("Категория", "Описание", [product])

    # Изменяем товар
    product.name = "Новое имя"
    product.price = 200.0

    # Проверяем, что изменения видны в категории
    assert category._Category__products[0].name == "Новое имя"
    assert category._Category__products[0].price == 200.0


def test_category_and_product_together() -> None:
    """Комплексный тест взаимодействия категории и товаров."""
    # Создаем несколько товаров
    products = []
    for i in range(3):
        product = Product(f"Товар {i}", f"Описание {i}", (i + 1) * 100.0, (i + 1) * 2)
        products.append(product)

    # Создаем категорию
    category = Category("Тестовая категория", "Тестовое описание", products)

    # Проверяем все атрибуты
    assert category.name == "Тестовая категория"
    assert category.description == "Тестовое описание"
    assert len(category._Category__products) == 3

    # Проверяем товары
    for i in range(3):
        assert category._Category__products[i].name == f"Товар {i}"
        assert category._Category__products[i].price == (i + 1) * 100.0
        assert category._Category__products[i].quantity == (i + 1) * 2


def test_add_product() -> None:
    """Проверка добавления продукта."""
    category = Category("Тест", "Описание", [])
    product = Product("Ноутбук", "Игровой", 100000.0, 3)

    # Добавляем продукт
    category.add_product(product)

    # Проверяем, что продукт в списке
    assert product.name in category.products, "Продукт должен быть в списке"


def test_products_getter() -> None:
    """Проверка геттера products."""
    product = Product("Планшет", "10 дюймов", 30000.0, 7)
    category = Category("Гаджеты", "Портативные", [product])

    # Проверяем формат вывода
    result = category.products
    expected_part = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."

    assert expected_part in result


def test_empty_category() -> None:
    """Проверка пустой категории."""
    category = Category("Пустая", "Нет товаров", [])

    assert category.products == "", "Пустая категория должна возвращать пустую строку"


def test_category_str(category: Category, products_list: List[Product]) -> None:
    """
    Проверяет, что метод __str__ возвращает строку вида:
    "Название категории, количество продуктов: сумма количеств товаров шт."
    """
    expected = "Тестовая категория, количество продуктов: 10 шт."
    assert str(category) == expected


def test_str_empty_category() -> None:
    """Проверяет строковое представление пустой категории."""
    empty_category = Category("Пустая", "Без товаров", [])
    expected = "Пустая, количество продуктов: 0 шт."
    assert str(empty_category) == expected
