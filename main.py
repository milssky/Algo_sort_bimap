from PIL import Image


def open_image(file_path:str) -> list[tuple[int,int,int]]:
    image = Image.open(file_path)
    return list(image.getdata())


def open_index_file(file_path:str) -> list[int]:
    with open(file_path) as file:
        indexes = list(map(int, file.readline()))
    return indexes


def my_sort(nums:list[int]) -> list[int]:
    pass


def main() -> None:
    list_of_pixel_colors = open_image('test_files/test.bmp')    
    pixels = open_index_file('test_files/test.txt')
    pixels = my_sort(pixels)

if __name__ == "__main__":
    main()

