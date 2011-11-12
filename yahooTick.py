#! /usr/bin/env python
# -*- coding: UTF-8 -*-

#<COPYLEFT>

import os
import sys
import urllib2

# this gets all yahoo data
#stat='l1c1va2xj1b4j4dyekjm3m4rr5p5p6s7'
# this only gets the price
#stat='sl1'
# relevant stuff

#currencies = ['USD', 'EUR', 'JPY', 'GBP', 'CHF', 'CAD', 'AUD', 'NZD'] 

def quotes():
    stat='l1d1t1'
    url = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s=X&f=%s'

    symbol = ['EURUSD', 'USDJPY', 'GBPUSD', 'USDAUD', 'USDCAD', 'CHFUSD', 'USDNZD']
    for i in symbol:
        qt=[i, urllib2.urlopen(url % (i, stat)).read().split(',')[0]]
        print(qt)

def hist():
    symbol = 'EURUSD'
    end_date = '20110902'
    start_date = '20010102'
    url = 'http://ichart.yahoo.com/table.csv?s=%s=X&' % symbol + \
          'd=%s&' % str(int(end_date[4:6]) - 1) + \
          'e=%s&' % str(int(end_date[6:8])) + \
          'f=%s&' % str(int(end_date[0:4])) + \
          'g=d&' + \
          'a=%s&' % str(int(start_date[4:6]) - 1) + \
          'b=%s&' % str(int(start_date[6:8])) + \
          'c=%s&' % str(int(start_date[0:4])) 
    days = urllib2.urlopen(url).readlines()
    data = [day.split(',')[:-2] for day in days]
    return data


if __name__ == '__main__':
    for i in hist():
        print(i)
    #quotes()


