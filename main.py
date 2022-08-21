from args_parser import parse_args
from path_handler import handle_path

args = parse_args()
direction = args.direction
paths = args.paths

image_paths = handle_path(paths)
print(image_paths)
