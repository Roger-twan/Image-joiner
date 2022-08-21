from argparse import ArgumentParser
from pathlib import Path, PosixPath
from termcolor import colored


def parse_args():
    parser = ArgumentParser(
        description='Join numerous images automatically'
    )
    parser.add_argument(
        'paths',
        nargs='*',
        help='File paths or directory path contains images',
        type=Path
    )
    parser.add_argument(
        '-d',
        '--direction',
        choices=['v', 'h', 'both'],
        help='v for vertical, h for horizontal (default is \'both\')'
    )

    args = parser.parse_args()

    if not args.paths:
        print(colored(
            'File paths were not given, set to default: [PosixPath(\'~/Downloads\')]', 'yellow'))
        args.paths = [PosixPath('~/Downloads')]
    else:
        print('Given file paths were:' +
              ''.join(map(lambda path: '\n - ' + str(path), args.paths)))

    if not args.direction:
        print(colored('Direction was not given, set to default: both', 'yellow'))
        args.direction = 'both'
    else:
        print(f'Given direction was: {args.direction}')

    return args
