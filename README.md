# Проект "ECommercePlatform"

## Описание:

Проект "ECommercePlatform" - это полнофункциональная платформа для
электронной коммерции, разработанная для обеспечения быстрых,
безопасных и приятных покупок в интернете. Проект создан с целью
предоставить бизнесу любого масштаба современное и гибкое
решение для онлайн-продаж.

## Цель проекта:

Основная цель проекта - упростить и удешевить создание профессиональных
онлайн-магазинов, предоставив разработчикам и бизнесу:
* Готовый набор ключевых функций (каталог, корзина, доставка)
* Гибкую архитектуру для интеграции
* Высокую производительность и оптимизацию
* Встроенные инструменты аналитики для управления бизнесом.

## Документация классов:

### `class BaseProduct(ABC)`
Абстрактный базовый класс для всех продуктов.

**Параметры инициализации:**
- `name` (str): Название товара.
- `description` (str): Описание товара.
- `price` (float): Цена товара.
- `quantity` (int): Количество товара в наличии.

**Основные методы:**

1. @property
   def price(self) -> float:
       """Геттер возвращает текущую цену товара."""
2. @price.setter
   def price(self, new_price: float) -> None:
       """Сеттер устанавливает новую цену товара. Проверяет, что цена положительная. При
       понижении цены запрашивает подтверждение у пользователя."""
3. def __str__(self) -> str:
        """Возвращает строку в формате: Название продукта, цена руб. Остаток: количество шт."""
4. @abstractmethod
   def __add__(self, other: "BaseProduct") -> float:
        """Абстрактный метод сложения товара — каждый наследник реализует свою логику."""
5. @classmethod
   @abstractmethod
   def new_product(
       cls, product_data: Dict[str, Any], products_list: Optional[Sequence["BaseProduct"]] = None
   ) -> "BaseProduct":
        """Абстрактный метод для корректного создания объектов с учётом дополнительных полей — 
        должен быть переопределён в наследниках."""

### class PrintMixin:
Класс-миксин для печати в консоль информации об объекте с указанием его класса и параметров.

**Параметры инициализации:**
- `name` (str): Название товара.
- `description` (str): Описание товара.
- `price` (float): Цена товара.
- `quantity` (int): Количество товара в наличии.

**Основные методы:** 

1. def __repr__(self) -> str:
        """Метод для отображения информации об объекте класса."""

### `class Product(BaseProduct, PrintMixin)`
Класс для представления продукции (наследник BaseProduct, PrintMixin).

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
       понижении цены запрашивает подтверждение у пользователя."""
4. def __str__(self) -> str:
        """Возвращает строку в формате: Название продукта, цена руб. Остаток: количество шт."""
5. def __add__(self, other: "Product") -> float:
        """Возвращает полную стоимость всех товаров на складе. Умножает стоимость и количество
        всех товаров в наличии. Вызывает ошибку TypeError при сложении объектов разных классов."""

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

print(str(product1))
print(str(product2))
print(str(product3))

print(product1 + product2)
print(product1 + product3)
print(product2 + product3)

### `class BaseEntity(ABC)`:
Абстрактный базовый класс для сущностей, имеющих название и описание.

**Параметры инициализации:**
- `name` (str): Название.
- `description` (str): Описание.

**Основные методы:**
1.  @abstractmethod
    def total_cost(self) -> float:
        """Абстрактный метод для вычисления общей стоимости. Должен быть переопределён
        в наследниках."""

### `class Category(BaseEntity)`
Класс для представления категорий продукции (наследник BaseEntity).

**Параметры инициализации:**
- `name` (str): Название категории.
- `description` (str): Описание категории.
- `products` (list): Список товаров категории.

**Переменные на уровне класса:**
- `category_count` (int): Количество категорий.
- `product_count` (int): Количество товаров.

**Основные методы:**
1. def add_product(self, product: Product) -> None:
       """Метод для добавления продукта в атрибут products. Вызывает ошибку TypeError при
       добавлении вместо продукта или его наследников любой другой объект."""
2. @property
   def products(self) -> str:
       """Геттер, который будет выводить список товаров в виде строк."""
3. def __str__(self) -> str:
        """Возвращает строку с названием категории и общим количеством всех продуктов."""
4. def total_cost(self) -> float:
        """Суммарная стоимость всех товаров в категории."""

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
print(str(category1))

print(category1.products)
print(str(category2))
print(category2.products)

smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

category_smartphones.add_product(smartphone3)

print(category_smartphones.products)

print(Category.product_count)

try:
category_smartphones.add_product("Not a product")  # type: ignore
except TypeError:
print("Возникла ошибка TypeError при добавлении не продукта")
else:
print("Не возникла ошибка TypeError при добавлении не продукта")

### `class ProductIterator`
Итератор для перебора товаров одной категории.

**Параметры инициализации:**
- `category_obj` (Category): Объект класса категории.
- `index` (int): Индекс.
- `products` (list): Список товаров категории.

**Основные методы:**
1. def __iter__(self) -> 'ProductIterator':
        """Возвращает итератор."""
2. def __next__(self) -> Product:
        """Возвращает следующий очередной товар категории."""

**Пример:**
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3],
)

iterator = ProductIterator(category1)

for product in iterator:
    print(product)
print()
for product in iterator:
    print(product)

### `class Smartphone(Product)`
Класс-наследник от базового класса Product.

**Параметры инициализации:**
- `name` (str): Название товара.
- `description` (str): Описание товара.
- `price` (float): Цена товара.
- `quantity` (int): Количество товара в наличии.
- `efficiency` (float): Производительность товара.
- `model` (str): Модель товара.
- `memory` (int): Объем встроенной памяти товара.
- `color` (str): Цвет товара.

**Основные методы:**
1. def __add__(self, other: BaseProduct) -> float:
        """Возвращает полную стоимость всех товаров на складе. Умножает стоимость и количество
        всех товаров в наличии. Вызывает ошибку TypeError при сложении объектов разных классов."""

**Пример:**
smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

print(smartphone1.name)
print(smartphone1.description)
print(smartphone1.price)
print(smartphone1.quantity)
print(smartphone1.efficiency)
print(smartphone1.model)
print(smartphone1.memory)
print(smartphone1.color)

print(smartphone2.name)
print(smartphone2.description)
print(smartphone2.price)
print(smartphone2.quantity)
print(smartphone2.efficiency)
print(smartphone2.model)
print(smartphone2.memory)
print(smartphone2.color)

print(smartphone3.name)
print(smartphone3.description)
print(smartphone3.price)
print(smartphone3.quantity)
print(smartphone3.efficiency)
print(smartphone3.model)
print(smartphone3.memory)
print(smartphone3.color)

smartphone_sum = smartphone1 + smartphone2
print(smartphone_sum)

grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

try:
invalid_sum = smartphone1 + grass1
except TypeError:
print("Возникла ошибка TypeError при попытке сложения")
else:
print("Не возникла ошибка TypeError при попытке сложения")

### `class LawnGrass(Product)`
Класс-наследник от базового класса Product.

**Параметры инициализации:**
- `name` (str): Название товара.
- `description` (str): Описание товара.
- `price` (float): Цена товара.
- `quantity` (int): Количество товара в наличии.
- `country` (str): Страна-производитель товара.
- `germination_period` (str): Срок прорастания товара.
- `color` (str): Цвет товара.

**Основные методы:**
1. def __add__(self, other: BaseProduct) -> float:
        """Возвращает полную стоимость всех товаров на складе. Умножает стоимость и количество
        всех товаров в наличии. Вызывает ошибку TypeError при сложении объектов разных классов."""

**Пример:**
grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

print(grass1.name)
print(grass1.description)
print(grass1.price)
print(grass1.quantity)
print(grass1.country)
print(grass1.germination_period)
print(grass1.color)

print(grass2.name)
print(grass2.description)
print(grass2.price)
print(grass2.quantity)
print(grass2.country)
print(grass2.germination_period)
print(grass2.color)

grass_sum = grass1 + grass2
print(grass_sum)

### class Order(BaseEntity):
Класс для представления заказа (один товар), наследник BaseEntity.

**Переменные на уровне класса:**

- `order_count` (int): Количество заказов.

**Параметры инициализации:**
- `name` (str): Название заказа (например, "Заказ №1").
- `description` (str): Описание заказа.
- `product` (str): Товар (объект класса Product или его наследника).
- `quantity` (int): Количество единиц товара.

**Основные методы:**
    
1. def total_cost(self) -> float:
        """Итоговая стоимость заказа."""

2. def __str__(self) -> str:
        """Возвращает строку с информацией о заказе."""

3. **Пример:**

# Создаем товары
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

# Создаем категорию
category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3],
    )
print(category1)
print(f"Общая стоимость товаров в категории: {category1.total_cost()} руб.")

# Создаем заказ
order = Order("Заказ №1", "Срочная доставка", product1, 2)
print(order)

## Использование классов:

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin
from src.product.py import Product
from src.base_entity import BaseEntity
from src.category.py import Category
from src.order import Order
from src.product_iterator.py import ProductIterator
from src.smartphone.py import Smartphone
from src.lawngrass.py import Lawngrass

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
    понижении цены запрашивает подтверждение у пользователя."""
8. **Метод __str__ рассчитывает общее количество товаров на складе**
def __str__(self) -> str:
    """Возвращает строку в формате: Название продукта, цена руб. Остаток: количество шт."""
9. **Метод сложения __add__ возвращает полную стоимость всех товаров на складе.**
def __add__(self, other: "Product") -> float:
    """Возвращает полную стоимость всех товаров на складе. Умножает стоимость и количество
    всех товаров в наличии."""
10. **Возвращает строку для класса Category**
def __str__(self) -> str:
    """Возвращает строку с названием категории и общим количеством всех продуктов."""
11. **Итератор для перебора товаров одной категории**    
def __iter__(self) -> 'ProductIterator':
    """Возвращает итератор."""
12. **Метод __next__ для перехода к следующему товару категории**     
def __next__(self) -> Product:
    """Возвращает следующий очередной товар категории."""
13. **Абстрактный метод для вычисления общей стоимости заказа**
@abstractmethod
def total_cost(self) -> float:
    """Абстрактный метод для вычисления общей стоимости. Должен быть переопределён
    в наследниках."""
14. **Абстрактный метод сложения товара**
@abstractmethod
def __add__(self, other: "BaseProduct") -> float:
    """Абстрактный метод сложения товара — каждый наследник реализует свою логику."""
15. **Абстрактный метод для корректного создания объектов**      
@classmethod
@abstractmethod
def new_product(
    cls, product_data: Dict[str, Any], products_list: Optional[Sequence["BaseProduct"]] = None
) -> "BaseProduct":
    """Абстрактный метод для корректного создания объектов с учётом дополнительных полей — должен быть
    переопределён в наследниках."""
16. **Расчет суммарной стоимости всех товаров в категории класса Category**    
def total_cost(self) -> float:
    """Суммарная стоимость всех товаров в категории."""
17. **Возвращает строку для класса Order**    
def __str__(self) -> str:
    """Возвращает строку с информацией о заказе."""
18. **Расчет итоговой стоимости заказа класса Order**    
def total_cost(self) -> float:
    """Итоговая стоимость заказа."""
19. **Печать информации об объекте класса**     
def __repr__(self) -> str:
        """Метод для отображения информации об объекте класса."""

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
*   `reset_counters`: сбрасывает счётчики категорий, продуктов и заказов перед каждым тестом.
*   `another_product`: содержит тестовые данные с другим товаром.
*   `category`: возвращает экземпляр класса Category с товарами.
*   `product_smartphone1`: содержит тестовые данные с примером первого экземпляра
     класса-наследника Smartphone.
*   `product_smartphone2`: содержит тестовые данные с примером второго экземпляра
     класса-наследника Smartphone.
*   `product_grass1`: содержит тестовые данные с примером первого экземпляра
     класса-наследника LawnGrass.
*   `product_grass2`: содержит тестовые данные с примером второго экземпляра
     класса-наследника LawnGrass.

## Параметризация

*   `test_add_product_invalid_type_raises_typeerror`: тестирует, что при попытке добавить
    объект, не являющийся экземпляром Product или его наследника, метод add_product выбрасывает
    TypeError с ожидаемым сообщением, и при этом состояние категории и общий счётчик продуктов
    не изменяются.

  
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
    pytest tests/test_product_iterator.py
    pytest tests/test_smartphone.py
    pytest tests/test_lawngrass.py
    pytest tests/test_base_intity.py
    pytest tests/test_base_product.py
    pytest tests/test_order.py
    pytest tests/test_print_mixin.py
    
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
