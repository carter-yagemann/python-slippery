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

"""Helper methods for configuring python-slippery to use a SOCKS5 proxy"""

import socks
import socket

def set_proxy(ip_addr, port):
    """Sets the SOCKS5 proxy.

    Args:
      ip_addr:
        The IP address of the SOCKS5 proxy.
      port:
        The port of the SOCKS5 proxy.
    """
    try:
        int(port)
    except ValueError as error:
        raise error
    socks.set_default_proxy(socks.SOCKS5, ip_addr, int(port))
    socket.socket = socks.socksocket
