from typing import Optional


class ZeroQuantityProduct(Exception):
    """Класс исключения для обработки событий, когда в «Категорию» или «Заказ» добавляется товар
     с нулевым количеством."""
    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(message)
