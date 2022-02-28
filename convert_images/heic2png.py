#!venv/bin/python

################################################################################
## Author: Lucas Matana Luza
##
## Description:
##  Simple script to convert HEIC files to PNG.
################################################################################

import sys, os
from PIL import Image
from pillow_heif import register_heif_opener
from tqdm import tqdm

register_heif_opener()

def print_usage():
    print('Wrong usage, please type \"heic2png.py -h\" for more info')
    sys.exit()

def print_help():
    print("Use: ./heic2png.py [input_dir] [output_dir]")
    sys.exit()

if len(sys.argv) == 1:
    print_usage()
elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print_help()
elif len(sys.argv) != 3:
    print_usage()
else:
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    files = sorted(os.listdir(input_dir))

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for img in tqdm(files, desc='Processing', colour='blue'):
        if '.heic' in img or '.HEIC' in img:
            image = Image.open(input_dir + img)
            image.save(output_dir + '/' + img[:-5] + '.png', format='png')