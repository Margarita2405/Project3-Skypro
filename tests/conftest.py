import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def sample_product():
    """Фикстура для создания тестового продукта."""
    return Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )

@pytest.fixture
def sample_category():
    """Фикстура с данными для создания категории."""
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [
            Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
        ]
    )


@pytest.fixture
def first_category():
    """Фикстура возвращает пример первой категории товаров для тестирования."""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        ]
    )


@pytest.fixture
def second_category():
    """Фикстура возвращает пример второй категории товаров для тестирования."""
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [
            Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
        ]
    )
