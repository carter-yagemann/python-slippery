#    Copyright 2016 Carter Yagemann
#
#    This file is part of python-slippery.
#
#    python-slippery is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    python-slippery is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with python-slippery.  If not, see <http://www.gnu.org/licenses/>.

import json
import urllib2
from slippery.burner_email import BurnerEmail
from slippery import proxy

def test_proxy(tor_test):
    if tor_test == '0':
        print 'Skipping tor test.'
        return
    
    data = urllib2.urlopen('https://api.ipify.org/?format=json').read()
    original_ip = json.loads(data)['ip']
    print 'Original IP:', original_ip
    
    proxy.set_proxy('localhost', 9050)
    
    data = urllib2.urlopen('https://api.ipify.org/?format=json').read()
    new_ip = json.loads(data)['ip']
    print 'New IP:', new_ip
    
    if new_ip == original_ip:
        print 'IPs are the same, proxy failed!'
        assert False
    
    email = BurnerEmail().generate()
    assert email._url != None
