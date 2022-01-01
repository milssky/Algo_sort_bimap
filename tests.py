import pytest
import inspect




#  TODO

def test_Pixel_class():
    try:
        import pixel
    except ModuleNotFoundError:
        assert False, "Нет такого файла - pixel.py"
    except NameError:
        assert False, "Файл должен называться - pixel.py"
    except ImportError:
        assert False, "Нет такого файла - pixel.py"

    assert hasattr(pixel, "Pixel"), (
            "Создайте класс Pixel"
        )
    assert inspect.isclass(pixel.Pixel), (
            "Pixel должен быть классом"
        )
    pixel = pixel.Pixel
    pixel_signature = inspect.signature(pixel)
    pixel_signature_list = list(pixel_signature.parameters)
    for p in ['x', 'y', 'color']:
        assert p in pixel_signature_list, (
                "У метода __init__ класса 'Pixel' должен быть "
                f"параметр {p}"
            )


def test_Bitmap_class():
    try:
        import bitmap
    except ModuleNotFoundError:
        assert False, "Нет такого файла - bitmap.py"
    except NameError:
        assert False, "Файл должен называться - bitmap.py"
    except ImportError:
        assert False, "Нет такого файла - bitmap.py"
    

def test_utils():
    try:
        import utils
    except ModuleNotFoundError:
        assert False, "Нет такого файла - utils.py"
    except NameError:
        assert False, "Файл должен называться - utils.py"
    except ImportError:
        assert False, "Нет такого файла - utils.py"
    

