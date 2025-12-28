from src.product import Product
from tests.conftest import first_category, second_category, sample_category


def test_category_init(first_category, second_category):
    """Тест, который проверяет корректность инициализации объектов класса Category."""
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, но и получения"
                                          " дополнительных функций для удобства жизни")
    assert len(first_category.products) == 3

    assert second_category.name == "Телевизоры"
    assert  second_category.description == ("Современный телевизор, который позволяет наслаждаться просмотром, станет"
                                            " вашим другом и помощником")
    assert len(second_category.products) == 1

    # Проверяем подсчет количества категорий
    assert first_category.category_count == 2
    assert second_category.category_count == 2

    # Проверяем подсчет количества товаров
    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_category_attributes(sample_category):
    """Тест наличия всех необходимых атрибутов класса Category."""
    # Проверяем name
    try:
        name = sample_category.name
        assert True  # Атрибут существует
    except AttributeError:
        assert False, "Атрибут 'name' отсутствует"

    # Проверяем description
    try:
        description = sample_category.description
        assert True
    except AttributeError:
        assert False, "Атрибут 'description' отсутствует"

    # Проверяем products
    try:
        products = sample_category.products
        assert isinstance(products, list)
    except AttributeError:
        assert False, "Атрибут 'products' отсутствует"


def test_products_in_category(sample_category):
    """Тест, что товары в категории являются объектами класса Product."""
    for product in sample_category.products:
        assert  isinstance(product, Product)
