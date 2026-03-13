from typing import List

import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


def test_iterator_returns_products_in_order(category_products: Category, products: List[Product]) -> None:
    """Проверяет, что итератор возвращает товары в том же порядке, в котором они хранятся в категории."""
    iterator = ProductIterator(category_products)
    for i, product in enumerate(iterator):
        assert product.name == products[i].name


def test_iterator_stop_iteration(category_products: Category) -> None:
    """Проверяет, что после перебора всех товаров выбрасывается StopIteration."""
    iterator = ProductIterator(category_products)
    # Перебираем все три товара
    for i in range(3):
        next(iterator)
    # Четвёртый вызов должен бросить StopIteration
    with pytest.raises(StopIteration):
        next(iterator)


def test_iterator_can_be_restarted(category_products: Category) -> None:
    """Проверяет, что можно повторно пройти по итератору (благодаря iter, который сбрасывает индекс)."""
    iterator = ProductIterator(category_products)
    first_pass = [product.name for product in iterator]
    second_pass = [product.name for product in iterator]
    assert first_pass == second_pass == ["A", "B", "C"]


def test_iterator_with_empty_category() -> None:
    """Проверяет поведение итератора для категории без товаров."""
    empty_category = Category("Пустая", "Без товаров", [])
    iterator = ProductIterator(empty_category)
    # При попытке получить первый элемент должно быть StopIteration
    with pytest.raises(StopIteration):
        next(iterator)
    # Цикл for не должен ничего вывести (но проверим, что не падает)
    collected = [product for product in iterator]
    assert collected == []
