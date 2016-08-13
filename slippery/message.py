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

"""A single message in an inbox"""

class Message(object):
    """Python class representing a single inbox message"""

    def __init__(self, sender, subject, body):
        """Initialize a message object.

            Args:
              sender:
                The sender of the email.
              subject:
                The subject of the email.
              body:
                The body of the email.
        """
        self._sender = sender
        self._subject = subject
        self._body = body

    def getsender(self):
        """Get the sender."""
        return self._sender

    def getsubject(self):
        """Get the subject."""
        return self._subject

    def getbody(self):
        """Get the body content."""
        return self._body
