import re
import sys
import time
from typing import List
from pathlib import Path, PosixPath
from termcolor import colored
from PIL import Image


def combine_images(
        paths: List[PosixPath],
        crop: str,
        direction: str,
        dest: PosixPath,
        name: str,
        image_type: str):
    if not paths:
        sys.exit(colored('There were no existing images discovered.', 'red'))
    elif (len(paths) == 1):
        sys.exit(colored('A single file doesn\'t need to be combined', 'red'))

    _images = [Image.open(image) for image in paths]
    _croppedImages = crop_images(_images, crop)

    if (direction is 'h' or direction is 'both'):
        save_image(combine_horizontal_images(_croppedImages),
                   dest, name, image_type, 'horizontal')
    if (direction is 'v' or direction is 'both'):
        save_image(combine_vertical_images(_croppedImages),
                   dest, name, image_type, 'vertical')


def crop_images(imgList: List, crop: str) -> List:
    _left, _top, _right, _bottom = tuple(list(map(int, crop.split(','))))

    return list(map(
        lambda img: img.crop((
            _left,
            _top,
            img.size[0] - _right,
            img.size[1] - _bottom)
        ), imgList))


def combine_horizontal_images(images: List) -> Image:
    _widths, _heights = zip(*(image.size for image in images))
    _total_width = sum(_widths)
    _max_height = max(_heights)

    _new_img = Image.new('RGB', (_total_width, _max_height), (255, 255, 255))
    _x_offset = 0
    for img in images:
        _new_img.paste(img, (_x_offset, 0))
        _x_offset += img.size[0]

    return _new_img


def combine_vertical_images(images: List) -> Image:
    _widths, _heights = zip(*(image.size for image in images))
    _max_width = max(_widths)
    _total_height = sum(_heights)

    _new_img = Image.new('RGB', (_max_width, _total_height), (255, 255, 255))
    _y_offset = 0
    for img in images:
        _new_img.paste(img, (0, _y_offset))
        _y_offset += img.size[1]

    return _new_img


def save_image(image: Image, dest: Path, name: str, image_type: str, direction: str):
    _dest_path = re.sub('^~', str(Path.home()), str(dest))
    _image_path = f'{_dest_path}/{name} - {direction}.{image_type}'
    _final_path = check_generate_file_name(_image_path)

    print(colored('Generating image...', 'blue'))
    _time_start = time.time()
    image.save(_final_path)
    _time_cost = format(time.time() - _time_start, '.2f')
    print(colored(
        f'Image was successfully generated: {_final_path}. Cost {str(_time_cost)} s.', 'green'))


def check_generate_file_name(file_path: str) -> str:
    if Path.exists(Path(file_path)):
        _new_path = '_.'.join(file_path.rsplit('.', 1))
        return check_generate_file_name(_new_path)
    else:
        return file_path
