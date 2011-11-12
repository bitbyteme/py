#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright <year> <copyright holder>. All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions 
# are met:

#    1. Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.

#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in 
#       the documentation and/or other materials provided with the
#       distribution.

# THIS SOFTWARE IS PROVIDED BY <COPYRIGHT HOLDER> ''AS IS'' AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
# THE POSSIBILITY OF SUCH DAMAGE.

# The views and conclusions contained in the software and documentation 
# are those of the authors and should not be interpreted as representing
# official policies, either expressed or implied, of <copyright holder>.


import urllib
import urllib2

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
req = urllib2.Request('http://www.goaogle.com')
try: 
    res = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
except TypeError, e:
    print e
else:
    print res.read()

n = 5
import numpy as np
print np.exp(np.linspace(-1., 0., n))


