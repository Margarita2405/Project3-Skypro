import json
import os

from typing import Any, List, Dict
from src.product import Product
from src.category import Category


def read_json(file_path: str) -> List[Dict[str, Any]]:
    """Функция, кторая принимает путь к файлу для загрузки данных из JSON файла и возвращает список словарей."""
    # Открываем файл для чтения
    with open(file_path, "r", encoding="UTF-8") as file:
        # Читаем данные из файла и преобразуем их из формата JSON в словарь Python
        data: List[Dict[str, Any]] = json.load(file)
    # Возвращаем полученный список словарей
    return data


def create_objects_from_json(data: List[Dict[str, Any]]) -> List[Category]:
    """Функция, которая принимает данные в виде списка словарей и создает объекты классов."""
    # Создаем пустой список для хранения объектов категорий
    categories: List[Category] = []
    # Начинаем цикл по каждой категории в данных
    for category in data:
        # Создаем пустой список для хранения товаров текущей категории
        products: List[Product] = []
        # Цикл по каждому товару внутри текущей категории
        for product in category["products"]:
            # Создаем объект Product и добавляем его в список товаров
            products.append(Product(**product))
        # Обновляем список товаров текущей категории на новый список объектов товаров
        category["products"] = products
        # Создаем объект Category и добавляем его в список категорий
        categories.append(Category(**category))
    # Возвращаем список объектов категорий
    return categories


if __name__ == "__main__":  # pragma: no cover
    # Формируем путь к файлу
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(current_dir, "data", "products.json")

    raw_data = read_json(file_path)
    categories_data = create_objects_from_json(raw_data)
    print(categories_data)
    print(categories_data[0].name)
    print(categories_data[0].description)
    print(categories_data[0].products)
    print(categories_data[1].name)
    print(categories_data[1].description)
    print(categories_data[1].products)
