#!/usr/bin/python3

"""Simple script to generate header comments based on user args.

Usage example:

- cmd:
python3 comment_header_generator.py -t 'Title' -c '#' -79

- output:
#################################### Title ####################################

- cmd:
python3 comment_header_generator.py -t 'Title' -c '#' -79 --title

- output:
###############################################################################
#################################### Title ####################################
###############################################################################
"""

__title__      = 'Comment Reader Generator'
__author__     = ['Lucas Matana Luza']
__copyright__  = 'Copyright (c) 2022 Lucas Matana Luza'
__license__    = 'MIT License'
__version__    = '0.1'
__maintainer__ = 'Lucas Matana Luza'
__email__      = 'lluza@live.com'
__status__     = 'Development'

###############################################################################
################################### Imports ###################################
###############################################################################

from sys import platform
import subprocess
import argparse

###############################################################################
################################### Parser ####################################
###############################################################################

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=__title__, 
    epilog=__doc__)
parser.add_argument('-v',
    action='version',
    version=f'Version: {__version__}')
parser.add_argument('-t',
    metavar='',
    help='Text to display in comment header.',
    required=False)
parser.add_argument('-c',
    metavar='',
    help='Comment character, e.g., # for python.',
    default='#',
    required=False)
parser.add_argument('-l',
    metavar='',
    help='The final numbers of characteres that will be presented in the' + \
        'comment line.',
    default='79',
    required=False)
parser.add_argument('--title',
    action='store_true',
    help='Create a top and bottom line with only comments characteres' + \
        'and the text value is in the middle line. ' + \
        'The final numbers of characteres that will be presented in the ' + \
        'comment line.',
    required=False)
args = parser.parse_args()

if not args.t:
    data = ''
else:
    data = ' ' + args.t + ' '

if args.title:
    output = f"{'':{args.c}^{args.l}}\n"
    output += f"{data:{args.c}^{args.l}}\n"
    output += f"{'':{args.c}^{args.l}}\n"
else:
    output = f"{data:{args.c}^{args.l}}"

print(output)

if platform == 'linux' or platform == 'linux2':
    p1 = subprocess.Popen(['echo', output], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['xclip', '-sel', 'clip'], stdin=p1.stdout)
elif platform == 'darwin':
    pass
elif platform == 'win32':
    pass
