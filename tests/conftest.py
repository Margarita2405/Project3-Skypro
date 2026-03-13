import json
from pathlib import Path
from typing import Generator, List

import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.order import Order
from src.product import Product
from src.smartphone import Smartphone


class TestProduct:
    """Тесты для класса Product."""


@pytest.fixture
def sample_product() -> Product:
    """Фикстура, возвращающая экземпляр класса Product для тестов."""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def another_product() -> Product:
    """Фикстура с другим товаром."""
    return Product("Другой товар", "Другое описание", 2000.0, 3)


class TestCategory:
    """Тесты для класса Category."""


@pytest.fixture(autouse=True)
def reset_counters() -> Generator[None, None, None]:
    """Сбрасывает счётчики категорий, продуктов и заказов перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0
    Order.order_count = 0
    yield


@pytest.fixture
def sample_category() -> Category:
    """Фикстура с данными для создания категории."""
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def first_category() -> Category:
    """Фикстура возвращает пример первой категории товаров для тестирования."""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def second_category() -> Category:
    """Фикстура возвращает пример второй категории товаров для тестирования."""
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def products_list() -> List[Product]:
    """Фикстура со списком товаров для категории."""
    return [
        Product("Товар 1", "Описание 1", 50.0, 3),
        Product("Товар 2", "Описание 2", 30.0, 7),
    ]


@pytest.fixture
def category(products_list: List[Product]) -> Category:
    """Фикстура, возвращающая экземпляр Category с товарами."""
    return Category("Тестовая категория", "Описание категории", products_list)


class TestProductIterator:
    """Тесты для класса ProductIterator."""


@pytest.fixture
def products() -> List[Product]:
    """Фикстура со списком товаров."""
    return [
        Product("A", "Описание A", 10.0, 1),
        Product("B", "Описание B", 20.0, 2),
        Product("C", "Описание C", 30.0, 3),
    ]


@pytest.fixture
def category_products(products: List[Product]) -> Category:
    """Фикстура категории с тремя товарами."""
    return Category("Тестовая категория", "Описание", products)


@pytest.fixture
def valid_data_content() -> str:
    """Фикстура возвращает строку с валидным JSON и представляет данные для тестирования успешного чтения файла."""
    return json.dumps(
        [
            {
                "name": "Смартфоны",
                "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций"
                "для удобства жизни",
                "products": [
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5,
                    },
                    {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                    {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
                ],
            },
            {
                "name": "Телевизоры",
                "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим"
                "другом и помощником",
                "products": [
                    {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
                ],
            },
        ]
    )


@pytest.fixture
def valid_data_file(tmp_path: Path, valid_data_content: str) -> str:
    """Фикстура создает временный файл с валидным JSON."""
    # Создаем файл в временной директории
    file_path = tmp_path / "valid_data.json"
    file_path.write_text(valid_data_content, encoding="utf-8")
    return str(file_path)


@pytest.fixture
def invalid_syntax_file(tmp_path: Path) -> str:
    """Фикстура создает временный файл с некорректным синтаксисом JSON. Содержимое файла: строка, которая
    не является валидным JSON."""
    file_path = tmp_path / "invalid_syntax.json"
    # Записываем некорректный JSON (нет закрывающей кавычки)
    file_path.write_text('{"name": "Тест", value: 123}', encoding="utf-8")
    return str(file_path)


@pytest.fixture
def empty_json_file(tmp_path: Path) -> str:
    """Фикстура создает пустой файл JSON. Пустой файл не является валидным JSON."""
    file_path = tmp_path / "empty.json"
    # Создаем пустой файл
    file_path.write_text("", encoding="utf-8")
    return str(file_path)


@pytest.fixture
def simple_valid_file(tmp_path: Path) -> str:
    """Фикстура создает простой валидный JSON файл. Используется для базового тестирования."""
    data = [{"name": "Тестовая категория", "products": [{"name": "Тестовый товар", "price": 100.0, "quantity": 5}]}]
    file_path = tmp_path / "simple_valid.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")
    return str(file_path)


@pytest.fixture
def nested_json_file(tmp_path: Path) -> str:
    """Создает файл с вложенными структурами."""
    file_path = tmp_path / "nested.json"
    data = [
        {
            "name": "Категория",
            "description": "Описание",
            "nested": {"level1": {"level2": "значение"}},
            "products": [
                {
                    "name": "Товар",
                    "description": "Описание",
                    "price": 100.0,
                    "quantity": 5,
                    "specs": {"color": "red", "size": ["S", "M", "L"]},
                }
            ],
        }
    ]
    file_path.write_text(json.dumps(data), encoding="utf-8")
    return str(file_path)


@pytest.fixture
def large_numbers_file(tmp_path: Path) -> str:
    """Создает файл с большими числами."""
    file_path = tmp_path / "large_numbers.json"
    data = [
        {
            "name": "Дорогие товары",
            "description": "Товары с высокой ценой",
            "products": [
                {"name": "Супер товар", "description": "Очень дорогой", "price": 1_000_000_000.0, "quantity": 1}
            ],
        }
    ]
    file_path.write_text(json.dumps(data), encoding="utf-8")
    return str(file_path)


@pytest.fixture
def special_chars_file(tmp_path: Path) -> str:
    """Создает файл со специальными символами."""
    file_path = tmp_path / "special_chars.json"
    data = [
        {
            "name": "Тест",
            "description": "тест & < > \" ' \n \t спецсимволы",
            "products": [
                {"name": "Товар & < >", "description": 'Описание с "кавычками"', "price": 100.0, "quantity": 5}
            ],
        }
    ]
    file_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return str(file_path)


@pytest.fixture
def product_smartphone1() -> Smartphone:
    """Фикстура для первого экземпляра класса-наследника Smartphone."""
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def product_smartphone2() -> Smartphone:
    """Фикстура для второго экземпляра класса-наследника Smartphone."""
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def product_grass1() -> LawnGrass:
    """Фикстура для первого экземпляра класса-наследника LawnGrass."""
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def product_grass2() -> LawnGrass:
    """Фикстура для второго экземпляра класса-наследника LawnGrass."""
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
