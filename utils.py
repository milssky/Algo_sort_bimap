from PIL import Image

from pixel import Pixel
from bitmap import Bitmap


def read_image(file_path:str) -> Bitmap:
    """Вычитывает изображение из BMP файла и возвращает объект-обертку над
    этим изображением."""
    image = Image.open(file_path)
    pixels:list[Pixel] = []
    for x in range(image.width):
        for y in range(image.height):
            pixels.append(Pixel(x,y, image.getpixel((x,y))))
    return Bitmap(pixels)


def read_index_files(file_path:str, width:int, height:int) -> list[int]:
    """Считывает из файла индексы пикселей в BMP файле."""
    with open(file_path) as file:
        nums = list(map(int, file.readline().split()))
    return nums


def my_sort() -> None:
    pass

