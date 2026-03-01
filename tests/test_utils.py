import pytest
import json

from pathlib import Path
from src.utils import read_json, create_objects_from_json
from src.product import Product
from src.category import Category


def test_read_json_valid_file(valid_data_file: str) -> None:
    """Тестирование успешного чтения валидного JSON файла."""
    # Читаем файл с помощью тестируемой функции
    data = read_json(valid_data_file)

    # Проверяем базовые условия
    assert data is not None, "Функция должна вернуть данные, а не None"
    assert isinstance(data, list), "Функция должна вернуть список"
    assert len(data) == 2, "В данных должно быть 2 категории"

    # Проверяем первую категорию
    first_category = data[0]
    assert first_category["name"] == "Смартфоны"
    assert first_category["description"] == (
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций"
        "для удобства жизни"
    )

    assert "products" in first_category, "В категории должен быть ключ 'products'"
    assert isinstance(first_category["products"], list), "products должен быть списком"
    assert len(first_category["products"]) == 3, "В категории должно быть 3 товара"

    # Проверяем первый товар в первой категории
    first_product = first_category["products"][0]
    assert first_product["name"] == "Samsung Galaxy C23 Ultra"
    assert first_product["description"] == "256GB, Серый цвет, 200MP камера"
    assert first_product["price"] == 180000.0
    assert first_product["quantity"] == 5

    # Проверяем вторую категорию
    second_category = data[1]
    assert second_category["name"] == "Телевизоры"
    assert len(second_category["products"]) == 1
    assert second_category["products"][0]["name"] == '55" QLED 4K'


def test_read_json_file_not_found() -> None:
    """Тестирование ошибки при попытке чтения несуществующего файла."""
    # Пытаемся прочитать несуществующий файл
    with pytest.raises(FileNotFoundError) as error_info:
        read_json("nonexistent.json")

    # Проверяем, что ошибка действительно произошла
    # Можно проверить текст ошибки, если нужно
    assert "No such file or directory" in str(error_info.value) or "не найден" in str(error_info.value)


def test_read_json_invalid_syntax(invalid_syntax_file: str) -> None:
    """Тестирование ошибки при чтении файла с некорректным синтаксисом JSON."""
    # Пытаемся прочитать файл с некорректным JSON
    with pytest.raises(json.JSONDecodeError) as error_info:
        read_json(invalid_syntax_file)

    # Проверяем, что ошибка действительно связана с JSON
    # В сообщении об ошибке должно быть что-то про парсинг
    assert "JSON" in str(error_info.value) or "Expecting" in str(error_info.value)


def test_read_json_empty_file(empty_json_file: str) -> None:
    """Тестирование чтения пустого файла."""
    # Пытаемся прочитать пустой файл
    with pytest.raises(json.JSONDecodeError) as error_info:
        read_json(empty_json_file)

    # Проверяем, что это ошибка парсинга JSON
    assert "Expecting value" in str(error_info.value)


def test_read_json_simple_case(simple_valid_file: str) -> None:
    """Простой тест для проверки базового функционала."""
    # Читаем файл
    data = read_json(simple_valid_file)

    # Проверяем результаты
    assert isinstance(data, list)
    assert len(data) == 1

    category = data[0]
    assert category["name"] == "Тестовая категория"
    assert len(category["products"]) == 1

    product = category["products"][0]
    assert product["name"] == "Тестовый товар"
    assert product["price"] == 100.0
    assert product["quantity"] == 5


def test_create_objects_from_json_simple() -> None:
    """Тестирование создания объектов из простых данных."""
    # Подготавливаем тестовые данные
    test_data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных"
            "функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]

    # Создаем объекты
    categories = create_objects_from_json(test_data)

    # Проверяем результаты
    assert isinstance(categories, list)
    assert len(categories) == 1

    # Проверяем категорию
    category = categories[0]
    assert isinstance(category, Category)
    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных" "функций для удобства жизни"
    )

    # Проверяем товары
    assert isinstance(category._Category__products, list)
    assert len(category._Category__products) == 1

    # Проверяем товар
    product = category._Category__products[0]
    assert isinstance(product, Product)
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_read_json_invalid_encoding(tmp_path: Path) -> None:
    """Тестирование чтения файла с неправильной кодировкой."""
    # Создаем файл в неправильной кодировке (например, UTF-16)
    file_path = tmp_path / "invalid_encoding.json"
    content = '{"test": "data"}'
    file_path.write_bytes(content.encode("utf-16"))

    # Попытка чтения с UTF-8 должна вызвать ошибку
    with pytest.raises(UnicodeDecodeError):
        read_json(str(file_path))


def test_read_json_nested_structures(nested_json_file: str) -> None:
    """Тестирование чтения файла с вложенными структурами."""
    data = read_json(nested_json_file)
    assert isinstance(data, list)
    # Проверяем, что вложенные структуры сохраняются
    assert isinstance(data[0].get("nested"), dict)


def test_read_json_large_numbers(large_numbers_file: str) -> None:
    """Тестирование чтения файла с большими числами."""
    data = read_json(large_numbers_file)
    assert isinstance(data, list)
    # Проверяем, что большие числа читаются правильно
    assert data[0]["products"][0]["price"] == 1_000_000_000.0


def test_read_json_special_characters(special_chars_file: str) -> None:
    """Тестирование чтения файла со специальными символами."""
    data = read_json(special_chars_file)
    assert isinstance(data, list)
    # Проверяем обработку специальных символов
    assert "тест & < > \" ' \n \t" in data[0]["description"]


def test_create_objects_from_json_empty_list() -> None:
    """Тестирование создания объектов из пустого списка."""
    # Передаем пустой список
    result = create_objects_from_json([])

    # Проверяем результаты
    assert isinstance(result, list)
    assert len(result) == 0


def test_create_objects_from_json_no_products_key() -> None:
    """Тестирование ошибки при отсутствии ключа 'products'."""
    # Данные без ключа 'products'
    invalid_data = [
        {
            "name": "Категория без товаров"
            # Нет ключа "products"
        }
    ]

    # Ожидаем KeyError при попытке доступа к category["products"]
    with pytest.raises(KeyError) as error_info:
        create_objects_from_json(invalid_data)

    # Проверяем, что ошибка связана с ключом 'products'
    assert "products" in str(error_info.value)


def test_create_objects_from_json_empty_products() -> None:
    """Тестирование создания категории с пустым списком товаров."""
    test_data = [{"name": "Пустая категория", "description": "Без товаров", "products": []}]  # Пустой список товаров

    categories = create_objects_from_json(test_data)

    assert len(categories) == 1
    category = categories[0]
    assert category.name == "Пустая категория"
    assert isinstance(category._Category__products, list)
    assert len(category.products) == 0


def test_create_objects_with_none_values() -> None:
    """Тестирование создания объектов с None значениями."""
    test_data = [
        {
            "name": None,
            "description": None,
            "products": [{"name": None, "description": None, "price": None, "quantity": None}],
        }
    ]

    categories = create_objects_from_json(test_data)
    assert len(categories) == 1
    assert categories[0].name is None
    assert categories[0]._Category__products[0].price is None


def test_create_objects_empty_category_name() -> None:
    """Тестирование создания категории с пустым именем."""
    test_data = [{"name": "", "description": "Описание", "products": []}]  # Пустое имя

    categories = create_objects_from_json(test_data)
    assert categories[0].name == ""


def test_create_objects_large_quantity() -> None:
    """Тестирование с большими значениями quantity."""
    test_data = [
        {
            "name": "Категория",
            "description": "Описание",
            "products": [
                {
                    "name": "Товар",
                    "description": "Описание",
                    "price": 100.0,
                    "quantity": 10_000_000,  # Большое количество
                }
            ],
        }
    ]

    categories = create_objects_from_json(test_data)
    assert categories[0]._Category__products[0].quantity == 10_000_000


def test_create_objects_malformed_products() -> None:
    """Тестирование с некорректным списком товаров."""
    test_data = [{"name": "Категория", "description": "Описание", "products": "not a list"}]  # Не список!

    with pytest.raises(TypeError):
        create_objects_from_json(test_data)


def test_create_objects_product_as_dict_instead_of_list() -> None:
    """Тестирование, когда products - один словарь, а не список."""
    test_data = [
        {
            "name": "Категория",
            "description": "Описание",
            "products": {  # Один товар как словарь, а не список
                "name": "Товар",
                "description": "Описание",
                "price": 100.0,
                "quantity": 5,
            },
        }
    ]

    with pytest.raises(TypeError):
        create_objects_from_json(test_data)


def test_create_objects_preserves_order() -> None:
    """Тестирование, что порядок категорий и товаров сохраняется."""
    test_data = [
        {
            "name": "Первая категория",
            "description": "Описание первой",
            "products": [
                {"name": "Товар 1", "description": "Описание", "price": 100, "quantity": 1},
                {"name": "Товар 2", "description": "Описание", "price": 200, "quantity": 2},
            ],
        },
        {
            "name": "Вторая категория",
            "description": "Описание второй",
            "products": [{"name": "Товар 3", "description": "Описание", "price": 300, "quantity": 3}],
        },
    ]

    categories = create_objects_from_json(test_data)
    assert len(categories) == 2
    assert categories[0].name == "Первая категория"
    assert categories[1].name == "Вторая категория"
    assert len(categories[0]._Category__products) == 2
    assert categories[0]._Category__products[0].name == "Товар 1"
    assert categories[0]._Category__products[1].name == "Товар 2"
    assert categories[1]._Category__products[0].name == "Товар 3"
