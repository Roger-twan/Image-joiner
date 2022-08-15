import argparse
import pathlib

def parse_args():
  parser = argparse.ArgumentParser(
    description='Join numerous images automatically'
  )
  parser.add_argument(
    'filepath',
    nargs='*',
    default='~/Downloads',
    help = 'File paths or directory contained images',
    type=pathlib.Path
  )
  parser.add_argument(
    '-d',
    '--direction',
    choices=['v', 'h', 'both'],
    default='both',
    help='v for vertical, h for horizontal (default is %(default)s)'
  )

  return parser.parse_args()
