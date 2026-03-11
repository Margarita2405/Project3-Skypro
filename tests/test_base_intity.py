import pytest
from src.base_entity import BaseEntity


def test_base_entity_cannot_be_instantiated() -> None:
    """Проверка, что BaseEntity является абстрактным и нельзя создать его экземпляр."""
    with pytest.raises(TypeError):
        BaseEntity("Имя", "Описание")  # type: ignore[abstract]


def test_category_is_subclass_of_base_entity(first_category: BaseEntity) -> None:
    """Проверка, что Category наследует BaseEntity."""
    assert isinstance(first_category, BaseEntity)
    assert issubclass(type(first_category), BaseEntity)
