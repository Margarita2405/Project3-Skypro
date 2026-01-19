from src.product import Product


def test_product_init(sample_product: Product) -> None:
    """Тест, который проверяет корректность инициализации объектов класса Product."""
    assert sample_product.name == "Samsung Galaxy S23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5


def test_product_attributes(sample_product: Product) -> None:
    """Тест наличия всех необходимых атрибутов класса Product."""
    # Проверяем name
    try:
        name = sample_product.name
        assert name is not None  # Атрибут существует
    except AttributeError:
        assert False, "Атрибут 'name' отсутствует"

    # Проверяем description
    try:
        description = sample_product.description
        assert description is not None  # Атрибут существует
    except AttributeError:
        assert False, "Атрибут 'description' отсутствует"

    # Проверяем price
    try:
        price = sample_product.price
        assert price is not None  # Атрибут существует
    except AttributeError:
        assert False, "Атрибут 'price' отсутствует"

    # Проверяем quantity
    try:
        quantity = sample_product.quantity
        assert quantity is not None  # Атрибут существует
    except AttributeError:
        assert False, "Атрибут 'quantity' отсутствует"


def test_product_init_default_values() -> None:
    """Тест инициализации с минимальными валидными значениями."""
    product = Product("Тест", "", 0.0, 0)

    assert product.name == "Тест"
    assert product.description == ""
    assert product.price == 0.0
    assert product.quantity == 0


def test_product_name_type(sample_product: Product) -> None:
    """Тест типа данных для атрибута name."""
    assert isinstance(sample_product.name, str), "name должен быть строкой"


def test_product_description_type(sample_product: Product) -> None:
    """Тест типа данных для атрибута description."""
    assert isinstance(sample_product.description, str), "description должен быть строкой"


def test_product_price_type(sample_product: Product) -> None:
    """Тест типа данных для атрибута price."""
    assert isinstance(sample_product.price, float), "price должен быть float"
    # Также price может быть int
    product_with_int_price = Product("Товар", "Тест", 100, 1)
    assert isinstance(product_with_int_price.price, (int, float)), "price должен быть числом"


def test_product_quantity_type(sample_product: Product) -> None:
    """Тест типа данных для атрибута quantity."""
    assert isinstance(sample_product.quantity, int), "quantity должен быть int"


def test_product_attribute_modification(sample_product: Product) -> None:
    """Тест изменения атрибутов после создания объекта."""
    # Изменяем все атрибуты
    sample_product.name = "Новое название"
    sample_product.description = "Новое описание"
    sample_product.price = 200000.0
    sample_product.quantity = 10

    # Проверяем изменения
    assert sample_product.name == "Новое название"
    assert sample_product.description == "Новое описание"
    assert sample_product.price == 200000.0
    assert sample_product.quantity == 10


def test_product_zero_price() -> None:
    """Тест создания продукта с нулевой ценой."""
    product = Product("Товар", "Описание", 0.0, 5)

    assert product.price == 0.0


def test_product_zero_quantity() -> None:
    """Тест создания продукта с нулевым количеством."""
    product = Product("Товар", "Описание", 100.0, 0)

    assert product.quantity == 0


def test_product_total_cost(sample_product: Product) -> None:
    """Тест для будущего метода расчета общей стоимости. Общая стоимость = цена * количество."""
    # Сейчас считаем вручную, в будущем может быть метод
    expected_total = sample_product.price * sample_product.quantity
    actual_total = sample_product.price * sample_product.quantity

    assert actual_total == expected_total
    assert actual_total == 180000.0 * 5  # 900000.0


def test_product_class_repr() -> None:
    """Тест строкового представления класса. Проверяем, что класс имеет понятное представление."""
    product = Product("Тест", "Описание", 100.0, 5)

    # Проверяем тип строкового представления
    assert isinstance(str(product), str)
    assert isinstance(repr(product), str)

    # Проверяем, что представление содержит имя класса
    assert "Product" in repr(product) or "Product" in str(product)
