import pytest

def test_product_init(sample_product):
    """Тест, который проверяет корректность инициализации объектов класса Product."""
    assert sample_product.name == "Samsung Galaxy S23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5


def test_product_attributes(sample_product):
    """Тест наличия всех необходимых атрибутов класса Product."""
    # Проверяем name
    try:
        name = sample_product.name
        assert True  # Атрибут существует
    except AttributeError:
        assert False, "Атрибут 'name' отсутствует"

    # Проверяем description
    try:
        description = sample_product.description
        assert True
    except AttributeError:
        assert False, "Атрибут 'description' отсутствует"

    # Проверяем price
    try:
        price = sample_product.price
        assert True
    except AttributeError:
        assert False, "Атрибут 'price' отсутствует"

    # Проверяем quantity
    try:
        quantity = sample_product.quantity
        assert True
    except AttributeError:
        assert False, "Атрибут 'quantity' отсутствует"
