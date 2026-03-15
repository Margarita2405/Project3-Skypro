from pytest import CaptureFixture

from src.product import Product


def test_print_mixin_on_creation(capsys: CaptureFixture[str]) -> None:
    """При создании объекта должен автоматически печататься его repr."""
    Product("Тест", "Описание", 100.0, 5)
    captured = capsys.readouterr()
    expected_repr = "Product('Тест', 'Описание', 100.0, 5)"
    assert expected_repr in captured.out


def test_repr_method() -> None:
    """Проверка метода repr, определённого в PrintMixin."""
    product = Product("Тест", "Описание", 100.0, 5)
    expected = "Product('Тест', 'Описание', 100.0, 5)"
    assert repr(product) == expected
