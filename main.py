from args_parser import parse_args
from path_handler import handle_path
from combine_images import combine_images

args = parse_args()
image_paths = handle_path(args.paths)
combine_images(
    paths=image_paths,
    crop=args.crop,
    direction=args.direction,
    dest=args.dest,
    name=args.name,
    image_type=args.image_type,
)
