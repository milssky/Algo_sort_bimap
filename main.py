from PIL import Image


OpenImageReturnType = tuple[list[tuple[int,int,int]], tuple[int, int], str] 


def open_image(file_path:str) -> OpenImageReturnType:
    image = Image.open(file_path)
    size = image.size
    mode = image.mode
    return list(image.getdata()), size, mode


def open_index_file(file_path:str) -> list[int]:
    with open(file_path) as file:
        indexes = list(map(int, file.readline().split()))
    return indexes


def my_sort(nums:list[int]) -> list[int]:
    return sorted(nums)


def get_colors_from_indexes(
        colors:list[tuple[int,int,int]], 
        indexes:list[int]
        ) -> list[tuple[int,int,int]]:
    return colors


def create_image(
        file_path:str, 
        colors:list[tuple[int,int,int]], 
        indexes:list[int],
        size: tuple[int, int],
        mode: str
    ) -> None:
    image = Image.new(mode, size)
    colors = get_colors_from_indexes(colors, indexes)
    image.putdata(colors)
    image.save(file_path)


def main() -> None:
    list_of_pixel_colors, size, mode = open_image('test_files/test.bmp')    
    pixel_indexes = open_index_file('test_files/test.txt')
    pixel_indexes = my_sort(pixel_indexes)
    create_image(
            'result.bmp', 
            list_of_pixel_colors, 
            pixel_indexes, 
            size, 
            mode
        )


if __name__ == "__main__":
    main()

