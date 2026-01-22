# Проект "ECommercePlatform"

## Описание:

Проект "ECommercePlatform" - это полнофункциональная платформа для
электронной коммерции, разработанная для обеспечения быстрых,
безопасных и приятных покупок в интернете. Проект создан с целью
предоставить бизнесу любого масштаба современное и гибкое
решение для онлайн-продаж.

## Цель проекта:

Основная цель проекта -упростить и удешевить создание профессиональных
онлайн-магазинов, предоставив разаработчикам и бизнесу:
* Готовый набор ключевых функций (каталог, корзина, доставка)
* Гибкую архитектуру для интеграции
* Высокую производительность и оптимизацию
* Встроенные инструменты аналитики для управления бизнесом.

## Документация классов:

### `class Product`
Класс для представления продукции.

**Параметры инициализации:**
- `name` (str): Название товара.
- `description` (str): Описание товара.
- `price` (float): Цена товара.
- `quantity` (int): Количество товара в наличии.

**Основные методы:**
1. @classmethod
   def new_product(cls, product_data: Dict[str, Any], products_list: Optional[List['Product']] = None) -> 'Product':
        """Класс-метод для создания объекта Product из словаря с параметрами. Проверяет
        наличие товара с таким же именем в списке products_list."""
2. @property
   def price(self) -> float:
       """Геттер возвращает текущую цену товара."""
3. @price.setter
   def price(self, new_price: float) -> None:
       """Сеттер устанавливает новую цену товара. Проверяет, что цена положительная. При
       понижении цены запрашивает потверждение у пользователя."""

**Пример:**
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
print(product1.name)
print(product1.description)
print(product1.price)
print(product1.quantity)

new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
print(new_product.name)
print(new_product.description)
print(new_product.price)
print(new_product.quantity)

### `class Category`
Класс для представления категорий продукции.

**Параметры инициализации:**
- `name` (str): Название категории.
- `description` (str): Описание категории.
- `products` (list): Список товаров категории.

**Переменные на уровне класса:**
- `category_count` (int): Количество категорий.
- `product_count` (int): Количество товаров.

**Основные методы:**
1. def add_product(self, product: Product) -> None:
       """Метод для добавления продукта в атрибут products."""
2. @property
   def products(self) -> str:
       """Геттер, который будет выводить список товаров в виде строк."""

**Пример:**
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
           180000.0, 5)
Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения
         дополнительных функций для удобства жизни",[product1])
print(category1.name == "Смартфоны")
print(category1.description)
print(len(category1.products))
print(category1.category_count)
print(category1.product_count)

## Использование классов:

from src.product.py import Product
from src.category.py import Category

## Функциональность:

1. **Получение данных из JSON-файла**
def read_json(file_path: str) -> List[Dict[str, Any]]:
    """Загружает данные о продукции из JSON-файла."""
2. **Создание объектов классов**
def create_objects_from_json(data: List[Dict[str, Any]]) -> List[Category]:
    """Функция, которая принимает данные в виде списка словарей и создает объекты классов."""
3. **Добавление товаров**
def add_product(self, product: Product) -> None:
    """Метод для добавления товара в атрибут products.""" 
4. **Вывод списка товаров в виде строк**
@property
def products(self) -> str:
    """Геттер, который будет выводить список товаров в виде строк."""
5. **Создание объекта Product из словаря с параметрами**
@classmethod
def new_product(cls, product_data: Dict[str, Any], products_list: Optional[List['Product']] = None) -> 'Product':
    """Класс-метод для создания объекта Product из словаря с параметрами. Проверяет наличие
    товара с таким же именем в списке products_list."""
6. **Возврат текущей цены товара**
@property
def price(self) -> float:
    """Геттер возвращает текущую цену товара."""
7. **Установка новой цены товара**
@price.setter
def price(self, new_price: float) -> None:
    """Сеттер устанавливает новую цену товара. Проверяет, что цена положительная. При
    понижении цены запрашивает потверждение у пользователя."""

## Использование функций:

from src.utils.py import read_json
from src.utils.py import create_objects_from_json

# Пример использования:

raw_data = read_json("data/products.json")
categories_data = create_objects_from_json(raw_data)

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Margarita2405/Project3-Skypro
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Настройте переменные окружения (скопируйте пример)
.env.example. Отредактируйте .env (ключи API, базы данных)

4. НАСТРОЙКИ API. API-ключ для:
```
Зарегистрируйтесь на https://apilayer.com/marketplace/ и получите бесплатный ключ
API_KEY=your_actual_api_key_here
```

## Тестирование

В этом разделе описываются процедуры тестирования для проекта.

# Цель тестирования

Этот раздел объясняет, зачем нужны тесты для данного проекта.

*   Тесты помогают обеспечить стабильность и качество кода.
*   Проверка функциональности и отсутствие регрессий.

# Использование

Для работы с проектом используются фикстуры в модуле 
conftest.py.

## Фикстуры

*   `sample_product`: содержит тестовые данные с описанием продукции.
*   `sample_category`: содержит тестовые данные с описанием категории продукции.
*   `first_category`: содержит тестовые данные с примером первой категории товаров. 
*   `second_category`: содержит тестовые данные с примером второй категории товаров. 

## Параметризация
  
# Подготовка к тестированию

Для запуска тестов необходимо выполнить следующие действия:

1. Установка зависимостей:
    ```
    pip install -r requirements.txt
    poetry add --group dev pytest
    poetry add --group dev pytest-cov
    poetry add requests
    ```
# Запуск тестов

1. Для запуска всех тестов используйте следующую команду в 
терминале: 
    ```
    pytest tests
    ```
2. Запуск тестов из конкретного файла:
    ```
    pytest tests/test_product.py
    pytest tests/test_category.py
    pytest tests/test_utils.py
    
    ```
3. Ожидаемый результат.
После успешного выполнения тестов вы должны увидеть вывод, 
подтверждающий, что все тесты успешно пройдены, например:
    ```
    === 10 passed in 0.01s ===
    ```
4. Если тесты не прошли.
Проверьте вывод команды на наличие ошибок.
Обратитесь к файлам тестов для анализа причин сбоев. 

5. Для запуска тестов с оценкой покрытия, используйте следующую
команду в терминале: 
    ```
    pytest --cov
    ```
6. Для создания отчета о покрытии в HTML-формате, используйте 
следующую команду в терминале: 
    ```
    pytest --cov=src --cov-report=html
    ```
## Логирование

### Файлы логов

### Настройка

## Документация:

Для получения дополнительной информации обратитесь 
к [документации](README.md).

## Лицензия

Этот проект распространяется под лицензией MIT.
