import os
from pathlib import Path, PosixPath
import re
import sys
from tarfile import SUPPORTED_TYPES
from typing import List
from termcolor import colored


def handle_path(paths: List[PosixPath]) -> List[PosixPath]:
    exist_paths = check_path(paths)

    if not exist_paths:
        sys.exit(colored('There were no existing files discovered.', 'red'))
    else:
        return find_image_files(exist_paths)


def check_path(paths: List[PosixPath]) -> List[PosixPath]:
    result = []

    for path in paths:
        real_path = Path(re.sub('^~', str(Path.home()), str(path)))
        if (real_path.exists()):
            result.append(real_path)
        else:
            print(colored('Given file or directory path not exist: ' + str(path), 'red'))

    return result


def find_image_files(paths: List[PosixPath]) -> List[PosixPath]:
    SUPPORTED_IMAGE_TYPES = ['.png', '.jpg', '.jpeg', '.gif']
    result = []

    if (len(paths) == 1):
        if paths[0].is_file():
            sys.exit(colored('A single file doesn\'t need to be joined', 'red'))
        elif (paths[0].is_dir()):
            for file in os.listdir(paths[0]):
                if (not file.startswith('.') and Path(file).suffix.lower() in SUPPORTED_IMAGE_TYPES):
                    result.append(Path.joinpath(paths[0], file))
            result.sort()
    else:
        if (len(list(filter(lambda path: path.is_dir(), paths))) > 0):
            sys.exit(colored(
                'Can\'t handle a mix of directions and files or multiple directions', 'red'))
        else:
            for path in paths:
                if (path.suffix.lower() in SUPPORTED_IMAGE_TYPES):
                    result.append(path)
                else:
                    print(
                        colored('Given path is not a image file: ' + str(path), 'red'))
    return result
