#! /usr/bin/env python
# -*- coding: UTF-8 -*-


import os
import sys


for arg in sys.argv[1:]:
    try: 
        f = os.stat(arg).st_mtime
        print str(f) + ' ' + arg

    except IndexError:
        err=2
        print 'EE(' + err + '): need to'
        sys.exit(2)





