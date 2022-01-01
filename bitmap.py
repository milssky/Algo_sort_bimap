from pixel import Pixel


class Bitmap:
    """Класс обертка для изображения."""
    def __init__(self, pixels: list[Pixel]) -> None:
        self.pixels = pixels

    
