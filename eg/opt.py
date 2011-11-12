#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# <COPYLEFT HERE>

import os
import subprocess
import sys
import urllib2

def interface():
    import argparse
    p = argparse.ArgumentParser(description='installing basic sys tools.')
    p.add = p.add_argument

    # defining options
    p.add('-i', '--install', action='store_true', help='installing all tools.')
    p.add('-u', '--upgrade', action='store_true', help='upgrade all tools.')
    p.add('-g', '--git', default='', metavar='URL', nargs='?' , help='sync git.')
    
    return(p.parse_args())


def whereis(prog):
    for i in os.environ.get('PATH').split(':'):
        cmd = os.path.join(i, prog)
        if os.path.exists(cmd) and not os.path.isdir(cmd):
            return(cmd)
    return None

def install():
    # checking/installing Xcode
    nix = subprocess
    run = subprocess.check_output
    if whereis('gcc-4.2') is None:
        err = 1
        cmd = ['open', '-a', 'Install Xcode']
        try: 
            run(cmd, stderr=nix.STDOUT)
        except nix.CalledProcessError, msg:
            print("Can't install Xcode, need to download it from Appstore.")
            sys.exit()
        else:
            print("After Xcode is done installing, run me again")
            sys.exit()

    # checking/installing homebrew
    if whereis('brew') is None:
        err = 2
        brewURL = 'https://raw.github.com/gist/323731'
        cmd = ['/usr/bin/ruby -e "$(curl -fsSL %s)"' % brewURL]
        try:
            run(cmd, stderr=nix.STDOUT, shell=True)
        except nix.CalledProcessError, msg:
            print('EE(%s): %s' % (err, msg.output))
            sys.exit(err)
        else:
            err = 3
            cmd = ['brew', 'update']
            try: 
                run(cmd, stderr=nix.STDOUT)
            except nix.CalledProcessError, msg:
                print('EE(%s): %s (%d)' % (err, msg.output))
                sys.exit(err)
    
    # checking/instaling for NEWER python
    err = 4
    python_version = 'Python 2.7.2'
    cmd = ['python', '--version']
    try: 
        tmp = nix.Popen(cmd, stdout=nix.PIPE, stderr=nix.PIPE)
    except OSError, msg:
        print('EE(%s): %s' % (err, msg))
        sys.exit(err)
    else:
        # for some reason, python reports its version into stderr
        if tmp.communicate()[1] != python_version:
            err = 5
            cmd = ['brew', 'install', 'wget']
            try: 
                run(cmd, stderr=nix.STDOUT)
            except nix.CalledProcessError, msg:
                print('EE(%s): %s' % (err, msg.output))
                sys.exit(err)


            
            
def update():
    nix = subprocess
    cmd = ['ls', '-l', 'eg']
    err = 2
    try: 
        ans = nix.check_output(cmd, stderr=nix.STDOUT)
    except OSError, msg:
        print('EE(%s): %s' % (err, msg))
        sys.exit(err)
    except nix.CalledProcessError, msg:
        print('EE(%s): %s' % (err, msg))
        sys.exit(err)
    else:
        return(ans)

    #nix = os.system
    #return(nix('brew list'))

def main():
    #print(' '.join(sys.argv) + '\n')
    #url = 'https://raw.github.com/bitbyteme/bin/master/installer.bash'
    
    args = interface()

    # --install, -i
    if args.install:
        print('installing')
    
    # --upgrade, -u
    if args.upgrade and not args.install:
        print('upgrading...')
    else:
        print('not upgrading')

    # --git, -g
    if args.git == '':
        print('not using git')
    elif args.git == None:
        print('using default gits')
    elif args.git != None:
        print("using '%s' git repo" % args.git)

if __name__ == '__main__':
    
    print(install())
    #print(whereis('gcc-4.2'))
    #print(update())
    sys.exit()
    
    try: main()
    except KeyboardInterrupt, msg:
        print(msg)
        sys.exit()

