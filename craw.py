#! /usr/bin/env python
# -*- coding: UTF-8 -*-

#<COPYLEFT>

import os
import re
import sys
import urllib2


target = 'http://ratedata.gaincapital.com/'

site = urllib2.urlopen(target).read()

print(site)




