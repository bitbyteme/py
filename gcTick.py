#! /usr/bin/env python
# -*- coding: UTF-8 -*-

#<COPYLEFT>

#
## This is a parser for Gain Capital historical data
#


import os
import sys
import pprint
import time
import datetime
from matplotlib import dates as mdates
from collections import OrderedDict
import redis


pp = pprint.PrettyPrinter(indent=1).pprint # print pretty
pb = os.fdopen(sys.stdout.fileno(), 'w', 0).write # print buffer
strptime = datetime.datetime.strptime

def interface():
    import argparse
    p = argparse.ArgumentParser(description='fixing Gain Capital data')
    p.add = p.add_argument
    p.add( '--files', '-f', default='', metavar='FILES', nargs='+',
            help='fixing files')
    return(p.parse_args())


def fix_numbers(i):
    try:return([(float(j)) for j in i])
    except ValueError: 
        return(float('nan')) 
    except KeyboardInterrupt, msg:
        print(' \nKeyboardInterrupt: 05')
        sys.exit()
    
def fix_time(t):
    # basic status dispplay. 
    # Need to replace with a better progress bar
    global count; count += 1
    if count % 1000 == 0: pb('.')
    
    time = t.pop(1)
    tmp00 = t[:]
    t = time.split('.') # separating milisec from time
    
    try: d = mdates.date2num(strptime(t[0], '%Y-%m-%d %H:%M:%S'))
    except KeyboardInterrupt, msg:
        print(' \nKeyboardInterrupt: 04')
        sys.exit()

    try: d = mdates.num2epoch(d) + float('.%s' % t[1]) 
    except IndexError:  d = mdates.num2epoch(d)
    finally:
        base = tmp00.pop(0)
        #r_server = redis.Redis('localhost')
        #r_server.set('name', 'DES')
        return([base, round(d, 3), fix_numbers(tmp00)])

def main(f):
    with open(f) as f:
        # parsing raw data
        f = [x.replace('\r\n', '').split(',')[-4:] for x in f.readlines()]

        # only official heading supported, so far!
        head = ['CurrencyPair', 'RateDateTime', 'RateBid', 'RateAsk']
        if f.pop(0) != head: raise 'Error' # have to create an exception!!
        
        # fixing data. converting ISO time into EPOCH and str into float
        global count; count = 0
        try: f = [(fix_time(x)) for x in f]
        except KeyboardInterrupt, msg:
            print(' \nKeyboardInterrupt: 02')
            sys.exit()
        else:
            d = {}
            for (base, time, price) in f:
                dd = OrderedDict([(time, price) for base, time, price in f ])
                d[base] = dd
                break
            return(d)

if __name__ == '__main__':
    def tmp00(f):
        print
        print(f)
        try: f = main(f)
        except KeyboardInterrupt, msg:
            print(' \nKeyboardInterrupt: 01')
            sys.exit()
        else: return(f)
    
    print('Total number of files: %s' % len(interface().files))
    #try: ans = [tmp00(f) for f in interface().files]
    try: ans = [tmp00(f) for f in interface().files]
    except KeyboardInterrupt, msg:
        print(' \nKeyboardInterrupt: 00')
        sys.exit()
    else: 
        # now that all files had been loaded and parsed, now merging 
        print('Final ans:')
        print
        d = {}
        #pairs = set([i.keys()[0] for i in ans ])
        #print(pairs)
        pp(ans)
        pp(len(ans))
        pp(type(ans))
    
    





    
