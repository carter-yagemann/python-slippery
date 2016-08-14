#!/usr/bin/env python
#
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

"""A library for interacting with the burner email webiste slippery.email"""

__author__ = 'Carter Yagemann'
__email__ = 'carter.yagemann@gmail.com'
__copyright__ = 'Copyright (c) 2016 Carter Yagemann'
__license__ = 'GPLv3'
__version__ = '1.0'
__url__ = 'https://bitbucket.org/carter-yagemann/python-slippery'
__download_url__ = 'https://bitbucket.org/carter-yagemann/python-slippery'
__description__ = 'A library for interacting with the slippery.email website'

import urllib
import socks
import socket

from .burner_email import BurnerEmail
