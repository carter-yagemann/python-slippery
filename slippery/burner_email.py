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

"""Creating and accessing burner emails is the core of python-slippery"""

import urllib
from slippery import validator, parser

def _gen_url(new_id, new_key):
    """Generate the inbox url from an id and key.

    Args:
      new_id:
        The id for the inbox.
      new_key:
        The key for the inbox.

    Return:
      The url which points to that inbox.
    """
    return 'http://slippery.email/inbox/' + new_id + '/' + new_key

def _gen_mailto(new_id):
    """Generate the mailto address from an id and key.

    Args:
      new_id:
        The id for the inbox.
      new_key:
        The key for the inbox.

    Return:
      The mailto address for that id.
    """
    return new_id + '@slipry.net'

def _gen_msg_base(new_id, new_key):
    """Generate the base url for messages from an id and key.

    Args:
      new_id:
        The id for the inbox.
      new_key:
        The key for the inbox.

    Return:
      The base url.
    """
    return 'http://slippery.email/message/' + new_id + '/' + \
           new_key + '/'

def _gen_del_url(inbox_id, inbox_key, msg_id):
    """Generate the url to delete a message.

    Args:
      inbox_id:
        The id for the inbox.
      inbox_key:
        The key for the inbox.
      msg_id:
        The id for the message.

    Return:
      The url which will delete the email as a string.
    """
    return 'http://slippery.email/app.php?i=' + inbox_id + '&p=' + \
           inbox_key + '&mode=delete&mid=' + msg_id

class BurnerEmail(object):
    """Python class representing a single slippery burner email"""

    def __init__(self):
        self._url = None
        self._id = None
        self._key = None
        self._mailto = None
        self._msg_base = None

    def setinbox(self, new_id, new_key):
        """Set the id and key for an email inbox.

        Args:
          new_id:
            The id for the new inbox.
          new_key:
            The new key for the inbox.
        """
        if not validator.validate_id(new_id):
            raise ValueError('id not valid.')
        if not validator.validate_key(new_key):
            raise ValueError('key not valid.')
        self._id = new_id
        self._key = new_key
        self._url = _gen_url(new_id, new_key)
        self._mailto = _gen_mailto(new_id)
        self._msg_base = _gen_msg_base(new_id, new_key)
        return self

    def generate(self):
        """Generate a burner email address and store the id and access key."""
        conn = urllib.urlopen('http://slippery.email/app.php?mode=create')
        if conn.getcode() != 200:
            raise OSError('Failed to connect to slippery.')
        self._url = conn.geturl()
        self._id = conn.geturl().split('/')[4]
        self._key = conn.geturl().split('/')[5]
        self._mailto = _gen_mailto(self._id)
        self._msg_base = _gen_msg_base(self._id, self._key)
        return self

    def getid(self):
        """Get the five digit id for the inbox."""
        return self._id

    def getkey(self):
        """Get the sixteen digit access key for the inbox."""
        return self._key

    def getmailto(self):
        """Get the email address."""
        return self._mailto

    def getinbox(self):
        """Get the full URL to access the email inbox."""
        return self._url

    def fetch_emails(self):
        """Generates a list of emails currently in the inbox.

        Return:
          An array of emails. Each email is a dictionary in the form:
            {'id':int, 'sender':str, 'subject':str, 'date':str}
        """
        conn = urllib.urlopen(self._url)
        if conn.getcode() != 200:
            raise OSError('Failed to connect to slippery.')
        return parser.parse_inbox(conn.read())

    def fetch_email(self, msg_id, msg_type='text'):
        """Fetches the body content of a single email.

        Args:
          msg_id:
            The id of the message. This can be found in the list generated
            by fetch_emails().
          msg_type:
            The body can either be returned as text (default) or HTML.
            Accepted values are 'text' and 'html'.

        Return:
          A string containing the body of the email.
        """
        if not msg_type in ['text', 'html']:
            raise ValueError("type must be 'text' or 'html'.")
        full_url = self._msg_base + msg_id + '/' + msg_type
        conn = urllib.urlopen(full_url)
        if conn.getcode() != 200:
            raise OSError('Failed to connect to slippery.')
        return parser.parse_message(conn.read(), msg_type)

    def delete_email(self, msg_id):
        """Deletes an email.

        Args:
          msg_id:
            The id of the message. This can be found in the list generated
            by fetch_emails().
        """
        del_url = _gen_del_url(self._id, self._key, msg_id)
        conn = urllib.urlopen(del_url)
        if conn.getcode() != 200:
            raise OSError('Failed to connect to slippery.')
