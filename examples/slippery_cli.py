#!/usr/bin/env python
#
#    Copyright 2016 Carter Yagemann
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""A command-line interface for slippery.email"""

import os
import sys

try:
    from slippery.burner_email import BurnerEmail
    from slippery import proxy
    import slippery.validator as validator
except ImportError:
    # slippery isn't installed, dev environment?
    sys.path.insert(0, os.path.abspath('.'))
    sys.path.insert(0, os.path.abspath('../'))
    from slippery.burner_email import BurnerEmail
    from slippery import proxy
    import slippery.validator as validator

def print_help():
    """Prints help information."""
    print 'NAME'
    print '       slippery_cli - Slippery CLI interface\n'
    print 'SYNOPSIS'
    print '       slippery_cli [COMMAND] [OPTIONS]\n'
    print 'COMMAND'
    print '       help'
    print '           Prints this message.\n'
    print '       create'
    print '           Creates a new burner email address.'
    print '       read'
    print '           Prompts the user to open an email from a list.'
    print '       delete'
    print '           Prompts the user to delete an email from a list.'
    print 'OPTIONS'
    print '       -i, -id'
    print '           The five character id for an inbox.\n'
    print '       -k, -key'
    print '           The sixteen character key for the inbox.\n'
    print '       -p, -proxy [ip_address:port]'
    print '           A SOCKS5 proxy to use.\n'

def parse_args(argv):
    """Parses a series of arguments.

    Args:
      argv:
        The array of arguments to parse.

    Return:
      A dictionary of arguments.
    """
    args = {}
    for i in range(len(argv)):
        if argv[i] == '-i' or argv[i] == '-id':
            if validator.validate_id(argv[i + 1]):
                args['id'] = argv[i + 1]
        elif argv[i] == '-k' or argv[i] == '-key':
            if validator.validate_key(argv[i + 1]):
                args['key'] = argv[i + 1]
        elif argv[i] == '-p' or argv[i] == '-proxy':
            if validate_proxy(argv[i + 1]):
                args['proxy_ip'] = argv[i + 1].split(':')[0]
                args['proxy_port'] = argv[i + 1].split(':')[1]
    return args

def validate_proxy(proxy_addr):
    """Validate a proxy address.

    Args:
      proxy_addr:
        The proxy address to validate.

    Return:
      True if it is a valid proxy address, otherwise False.
    """
    parts = proxy_addr.split(':')
    if len(parts) != 2:
        return False
    try:
        int(parts[1])
        return True
    except ValueError:
        return False

def create(args):
    """Create a new burner email address.

    Args:
      args:
        A dictionary of arguments produced by parse_args().
    """
    if 'proxy_ip' in args.keys() and 'proxy_port' in args.keys():
        print 'Using proxy ' + args['proxy_ip'] + ':' + args['proxy_port']
        proxy.set_proxy(args['proxy_ip'], int(args['proxy_port']))
    email = BurnerEmail().generate()
    print 'Burner email generated:', email.getmailto()
    print 'Use the following arguments in future commands to use this email:'
    print '    -i ' + email.getid() + ' -k ' + email.getkey()

def read(args):
    """Allows the user to open an email from the inbox.

    Args:
      args:
        A dictionary of arguments produced by parse_args().
    """
    if 'proxy_ip' in args.keys() and 'proxy_port' in args.keys():
        print 'Using proxy ' + args['proxy_ip'] + ':' + args['proxy_port']
        proxy.set_proxy(args['proxy_ip'], int(args['proxy_port']))
    if not 'id' in args:
        print "Please specify an inbox id with the -i flag. Did you run create?"
        return
    if not 'key' in args:
        print "Please specify a key with the -k flag. Did you run create?"
        return
    email = BurnerEmail().setinbox(args['id'], args['key'])
    msgs = email.fetch_emails()
    if len(msgs) == 0:
        print 'You have no emails!'
        return
    for msg in range(len(msgs)):
        msg_data = msgs[msg]
        print str(msg) + ':', msg_data['sender'], '//', msg_data['subject'], \
              '//', msg_data['date']
    print '\nWhich email would you like to read? (q to quit)'
    sys.stdout.write('> ')
    try:
        pick = int(raw_input())
    except ValueError:
        return
    if pick >= len(msgs) or pick < 0:
        print 'Invalid index'
        return
    print email.fetch_email(msgs[pick]['id'])

def delete(args):
    """Allows the user to delete an email from the inbox.

    Args:
      args:
        A dictionary of arguments produced by parse_args().
    """
    if 'proxy_ip' in args.keys() and 'proxy_port' in args.keys():
        print 'Using proxy ' + args['proxy_ip'] + ':' + args['proxy_port']
        proxy.set_proxy(args['proxy_ip'], int(args['proxy_port']))
    if not 'id' in args:
        print "Please specify an inbox id with the -i flag. Did you run create?"
        return
    if not 'key' in args:
        print "Please specify a key with the -k flag. Did you run create?"
        return
    email = BurnerEmail().setinbox(args['id'], args['key'])
    msgs = email.fetch_emails()
    if len(msgs) == 0:
        print 'You have no emails!'
        return
    for msg in range(len(msgs)):
        msg_data = msgs[msg]
        print str(msg) + ':', msg_data['sender'], '//', msg_data['subject'], \
              '//', msg_data['date']
    print '\nWhich email would you like to delete? (q to quit)'
    sys.stdout.write('> ')
    try:
        pick = int(raw_input())
    except ValueError:
        return
    if pick >= len(msgs) or pick < 0:
        print 'Invalid index'
        return
    email.delete_email(msgs[pick]['id'])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
    elif sys.argv[1] == 'create':
        create(parse_args(sys.argv[2:]))
    elif sys.argv[1] == 'read':
        read(parse_args(sys.argv[2:]))
    elif sys.argv[1] == 'delete':
        delete(parse_args(sys.argv[2:]))
    else:
        print_help()
