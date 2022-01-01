from dataclasses import dataclass


@dataclass
class Pixel:
    """Класс, отражающий пиксель изображения."""
    x:int
    y:int
    color:int

