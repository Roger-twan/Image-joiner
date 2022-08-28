# Image Jointer
A simple python script for combining several images
## How to use
```bash
python main.py [file paths] [-h] [-d {v,h,both}] [-c CROP] [--dest DEST] [-n NAME]
```
Parameters specifications
| parameter | full parameter | description |
| --- | --- | --- |
| file paths | - | image paths or directory (default is [PosixPath('~/Downloads')]) |
| -h | --help | show help message |
| -d | --direction | {v,h,both} v for vertical, h for horizontal (default is 'both') |
| -c | --crop | Crop each image from left, top, right, bottom (default is 0,0,0,120) |
| -dest | - | Specify the direction of generated image (default is PosixPath('~/Downloads'))
| -n | --name | Specify the name of generated image (default is untitled) |
| -t | --image_type | Specify the type of generated image (default is png) |


## How to Startup
1. create and activate virtual environment
```bash
python3 -m venv env
source env/bin/activate
```

2. install packages
```bash
pip install -r requirements.txt
```

3. run script
```bash
python main.py ...
```
