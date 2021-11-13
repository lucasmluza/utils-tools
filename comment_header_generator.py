#!/usr/bin/python3

import sys
import subprocess

def print_usage():
    print('Wrong usage, please type \"comment_header_generator.py -h\" for more info')
    sys.exit()

def print_help():
    print("Use: .comment_header_generator.py [data] [symbol] [lenght]")
    print("Obs: the ouptut will be at your clipboard")
    sys.exit()

if len(sys.argv) == 1:
    print_usage()
elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print_help()
elif len(sys.argv) != 4:
    print_usage()
else:
    data = sys.argv[1]
    if data != '':
        data = ' ' + data + ' '
    c = sys.argv[2]
    n = sys.argv[3]

    output = ('{data:{c}^{n}}'.format(
            data = data,
            c = c,
            n = n
        )
    )
    print(output)
    p1 = subprocess.Popen(["echo", output], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["xclip", "-sel", "clip"], stdin=p1.stdout)
    #cmd = f'echo {output} | xclip -sel clip'
    #subprocess.check_output(["bash", "-c", cmd])
    #subprocess.run(cmd, shell=True)
