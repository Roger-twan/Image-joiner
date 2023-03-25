import os
from pathlib import Path, PosixPath
import re
import sys
from tarfile import SUPPORTED_TYPES
from typing import List
from termcolor import colored


def handle_path(paths: List[PosixPath]) -> List[PosixPath]:
    _exist_paths = check_path(paths)

    if not _exist_paths:
        sys.exit(colored('There were no existing files discovered.', 'red'))
    else:
        return find_image_files(_exist_paths)


def check_path(paths: List[PosixPath]) -> List[PosixPath]:
    _result = []

    for path in paths:
        _real_path = Path(re.sub('^~', str(Path.home()), str(path), 1))
        if (_real_path.exists()):
            _result.append(_real_path)
        else:
            print(colored('Given file or directory path not exist: ' + str(path), 'red'))

    return _result


def find_image_files(paths: List[PosixPath]) -> List[PosixPath]:
    SUPPORTED_IMAGE_TYPES = ['png', 'jpg', 'jpeg', 'gif', 'webp']
    _result = []

    if (len(paths) == 1):
        if paths[0].is_file():
            sys.exit(colored('A single file doesn\'t need to be combined', 'red'))
        elif (paths[0].is_dir()):
            for file in os.listdir(paths[0]):
                if (not file.startswith('.') and Path(file).suffix.lower()[1:] in SUPPORTED_IMAGE_TYPES):
                    _result.append(Path.joinpath(paths[0], file))
            _result.sort()
    else:
        if (len(list(filter(lambda path: path.is_dir(), paths))) > 0):
            sys.exit(colored(
                'Can\'t handle a mix of directions and files or multiple directions', 'red'))
        else:
            for path in paths:
                if (path.suffix.lower() in SUPPORTED_IMAGE_TYPES):
                    _result.append(path)
                else:
                    print(
                        colored('Given path is not a image file: ' + str(path), 'red'))
    return _result
