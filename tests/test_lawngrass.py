import pytest

from src.lawngrass import LawnGrass


def test_grass_product_init(product_grass1: LawnGrass) -> None:
    """Тест проверяет корректность инициализации объектов класса Lawngrass."""
    assert product_grass1.name == "Газонная трава"
    assert product_grass1.description == "Элитная трава для газона"
    assert product_grass1.price == 500.0
    assert product_grass1.quantity == 20
    assert product_grass1.country == "Россия"
    assert product_grass1.germination_period == "7 дней"
    assert product_grass1.color == "Зеленый"


def test_grass_product_add(product_grass1: LawnGrass, product_grass2: LawnGrass) -> None:
    """Тест проверяет сложение товаров только из одинаковых классов продуктов."""
    assert product_grass1 + product_grass2 == 16750.0


def test_grass_product_add_error(product_grass1: LawnGrass) -> None:
    """Тест проверяет, что при сложении объектов разных классов выбрасывается ошибка TypeError."""
    with pytest.raises(TypeError):
        product_grass1 + 1  # type: ignore[operator]
