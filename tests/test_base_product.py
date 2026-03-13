import pytest
from pytest import CaptureFixture

from src.base_product import BaseProduct
from src.product import Product


def test_base_product_abstract() -> None:
    """Проверка, что BaseProduct является абстрактным и нельзя создать его экземпляр."""
    with pytest.raises(TypeError):
        BaseProduct("Имя", "Описание", 100.0, 5)  # type: ignore[abstract]


def test_product_is_subclass_of_base_product() -> None:
    """Проверка, что Product наследует BaseProduct."""
    assert issubclass(Product, BaseProduct)


def test_product_initialization() -> None:
    """Проверка инициализации продукта (конструктор BaseProduct)."""
    product = Product("Тест", "Описание", 100.0, 5)
    assert product.name == "Тест"
    assert product.description == "Описание"
    assert product.price == 100.0
    assert product.quantity == 5


def test_price_getter() -> None:
    """Геттер price должен возвращать корректное значение."""
    product = Product("Тест", "Описание", 100.0, 5)
    assert product.price == 100.0


def test_str_method() -> None:
    """Проверка строкового представления продукта (унаследовано от BaseProduct)."""
    product = Product("Тест", "Описание", 100.0, 5)
    expected = "Тест, 100.0 руб. Остаток: 5 шт."
    assert str(product) == expected


def test_price_setter_positive() -> None:
    """Установка положительной цены (без понижения)."""
    product = Product("Тест", "Описание", 100.0, 5)
    product.price = 150.0
    assert product.price == 150.0


def test_price_setter_non_positive(capsys: CaptureFixture[str]) -> None:
    """Попытка установить неположительную цену не должна менять цену и должна выводить сообщение."""
    product = Product("Тест", "Описание", 100.0, 5)
    product.price = -10
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0  # цена не изменилась

    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0
