import pytest

from src.smartphone import Smartphone


def test_smartphone_product_init(product_smartphone1: Smartphone) -> None:
    """Тест проверяет корректность инициализации объектов класса Smartphone."""
    assert product_smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone1.price == 180000.0
    assert product_smartphone1.quantity == 5
    assert product_smartphone1.efficiency == 95.5
    assert product_smartphone1.model == "S23 Ultra"
    assert product_smartphone1.memory == 256
    assert product_smartphone1.color == "Серый"


def test_smartphone_product_add(product_smartphone1: Smartphone, product_smartphone2: Smartphone) -> None:
    """Тест проверяет сложение товаров только из одинаковых классов продуктов."""
    assert product_smartphone1 + product_smartphone2 == 2580000.0


def test_smartphone_product_add_error(product_smartphone1: Smartphone) -> None:
    """Тест проверяет, что при сложении объектов разных классов выбрасывается ошибка TypeError."""
    with pytest.raises(TypeError):
        product_smartphone1 + 1  # type: ignore[operator]
