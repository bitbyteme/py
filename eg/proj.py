#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# <COPYLEFT HERE>

import os
import sys
import optparse
import copy
import urllib2

class MyOption(optparse.Option):
    def check_url_status(option, opt, value):
        try: 
            urllib2.urlopen(value)
        except ValueError: 
            raise optparse.OptionValueError(
                    "option %s: \n\tURL format invalid: <%s>" % (opt, value))
        except urllib2.HTTPError:
            raise optparse.OptionValueError(
                    "option %s: \n\tURL does not exit: <%s>" % (opt, value))

    TYPES = optparse.Option.TYPES + ('URL',)
    TYPE_CHECKER = copy.copy(optparse.Option.TYPE_CHECKER)
    TYPE_CHECKER['URL'] = check_url_status

def interface(args):
    def optional(option, opt_str, value, parser):
        if parser.values.git:
            raise OptionValueError('xxxx')
        setattr(parser.values, option.dest, value)
        
    p = optparse.OptionParser(option_class=MyOption)
    
    # --upgrade, -u
    help_msg = 'upgrade all extra tools.'
    p.add_option('--upgrade', '-u', action='store_false', help=help_msg) 
    
    # --git -u
    url = 'https://raw.github.com/bitbyteme/bin/master/installer.bash'
    help_msg = 'by default, sync a git according with $GITURL.'
    p.add_option('--git', '-g',  metavar='URL', type='URL', help=help_msg,
            action='callback', callback=optional, dest='git')
    
    return(p.parse_args())

def main(args):
    (opt, arg) = interface(args)
    
    # --upgrade, -u
    if opt.upgrade == None:
        print('Not upgrading')
    else:
        print('upgrading')

    # --git, -g
    if opt.git == None:
        print('not syncing with github')
    elif opt.git == False:
        try: giturl = os.environ['GITURL']
        except KeyError, errMsg: 
            errStatus, repo = 1, opt.git
            print('EE(%s): global variable %s not set, using %s' % 
                    (errStatus, errMsg, repo))
            sys.exit(errStatus)
    else:
        print(opt.git)
    #


if __name__ == '__main__':
    try: main(sys.argv)
    except KeyboardInterrupt, msg:
        print(msg)
        sys.exit()






