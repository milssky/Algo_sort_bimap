from pixel import Pixel
from typing import Callable


class Bitmap:
    """Класс обертка для изображения."""
    def __init__(self, pixels: list[Pixel]) -> None:
        self.pixels = pixels

    def sort_index(self, sort_function: Callable[list[Pixel]]) -> None:
        """Сортирует пиксели алгоритмом из sort_function."""
        pass

    def save_bitmap(self, name:str = "solution.bmp") -> None:
        """Сохраняет пиксели в файл name.bmp."""
        pass

