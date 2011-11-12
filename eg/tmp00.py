#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import time

def mtime(f):
    try: return(os.stat(f).st_mtime)
    except OSError, msg:
        print(msg)
        sys.exit(1)

def main():
    nix = os.system
    old = 0
    f = sys.argv[1]
    while True:
        if old != mtime(f):
            old = mtime(f)
            print('=')
            nix('python ' + f)
        time.sleep(1)

try: main()
except KeyboardInterrupt, msg:
    print(msg)
    sys.exit()
except IndexError, msg:
    sys.exit()









#from collections import OrderedDict as dict
#d = dict([('fisrt', 1),
#    ('second', 2),
#    ('third', 3)])

#d['second'] = 4
#del d['second']
#d['second'] = 5

#print(d.items())


