from argparse import ArgumentParser
from pathlib import Path, PosixPath
from termcolor import colored


def parse_args():
    parser = ArgumentParser(
        description='Join several images automatically'
    )
    parser.add_argument(
        'paths',
        nargs='*',
        help='File paths or directory path contains images (default is [PosixPath(\'~/Downloads\')])',
        type=Path
    )
    parser.add_argument(
        '-d',
        '--direction',
        choices=['v', 'h', 'both'],
        help='v for vertical, h for horizontal (default is \'both\')',
        type=str
    )
    parser.add_argument(
        '-c',
        '--crop',
        help='Crop each image from left, top, right, bottom (default is 0,0,0,120)',
        type=str
    )
    parser.add_argument(
        '--dest',
        help='Specify the direction of generated image (default is PosixPath(\'~/Downloads\'))',
        type=Path
    )
    parser.add_argument(
        '-n',
        '--name',
        help='Specify the name of generated image (default is untitled))',
        type=str
    )
    parser.add_argument(
        '-t',
        '--image_type',
        help='Specify the type of generated image (default is png))',
        type=Path
    )

    return set_default_args(parser.parse_args())


def set_default_args(args):
    _args = args
    DEFAULT_ARGS = {
        'paths': [PosixPath('~/Downloads')],
        'direction': 'both',
        'crop': '0,0,0,120',
        'dest': PosixPath('~/Downloads'),
        'name': 'untitled',
        'image_type': 'png'
    }

    for arg in vars(_args):
        if not getattr(_args, arg):
            print(colored(f'Argument {arg} was not given, set to default: {str(DEFAULT_ARGS[arg])}', 'yellow'))
            setattr(_args, arg, DEFAULT_ARGS[arg])
        else:
            print(f'Given {arg} was: {getattr(_args, arg)}')

    return _args
